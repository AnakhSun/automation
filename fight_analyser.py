from services.vk_service import VKService

class FightAnalyser():
    def __init__(self) -> None:
        self.vk = VKService()
        
    def run(self) -> None:
        print("fight is running")