from typing import Callable, Any, Optional
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from python3_anticaptcha import ImageToTextTask
from config import Config

class VKService():
    """Handles VK API interactions"""
    
    def __init__(self):
        self.session = self._create_session()
        self.api = self.session.get_api()
        self.longpoll = VkLongPoll(self.session)

    def _create_session(self) -> vk_api.VkApi:
        """Creates and configures VK session"""
        return vk_api.VkApi(
            token=Config.VK_TOKEN,
            captcha_handler=self._handle_captcha
        )
    
    def _handle_captcha(self, captcha: Any) -> Any:
        """Handles captcha challenges using anti-captcha service"""
        key = ImageToTextTask.ImageToTextTask(
            anticaptcha_key=Config.ANTICAPTCHA_TOKEN,
            save_format='const'
        ).captcha_handler(captcha_link=captcha.get_url())
        
        return captcha.try_again(key['solution']['text'])

    def send_message(self, id: int, message: str, 
                    forward_message_id: Optional[int] = None) -> int:
        """Sends message to VK chat"""
        params = {
            "peer_id": id,
            "message": message,
            "random_id": 0
        }
        
        if forward_message_id:
            params["forward_messages"] = forward_message_id
            
        return self.session.method("messages.send", params)

    def delete_message(self, message_id: int) -> None:
        """Deletes message by ID"""
        self.session.method("messages.delete", {
            "message_ids": message_id,
            "delete_for_all": 1
        })

    def buttons_getter(self) -> list: 
        sorted_buttons_temp = []
        message = self.api.messages.getConversationsById(peer_ids = Config.GROUP_ID)
        if 'current_keyboard' in message['items'][0]:
            all_buttons = message['items'][0]['current_keyboard']['buttons']
            for current_button in all_buttons:
                for button_property in range(len(current_button)):
                    current_button_name = current_button[button_property]['action']['label']
                    current_button_type = current_button[button_property]['color']
                    current_button_payload = current_button[button_property]['action']['payload']
                    sorted_buttons_temp.append((current_button_name.lower(), current_button_type.lower(), current_button_payload))
            return sorted_buttons_temp
        return []

    def listen_events(self, callback: Callable[[VkEventType], None]) -> None:
        """Listens for VK events and processes them"""
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.from_group and event.group_id == abs(int(Config.GROUP_ID)) and not event.from_me:
                    callback(event)

    
        