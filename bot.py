from services.vk_service import VKService
from utils.text_processing import replace_letters
import events

class Bot():
    def __init__(self) -> None:
        self.vk = VKService()
        
    def handle_event(self, event) -> str:
        gmt = replace_letters(event.text.lower())
        event = events.Event(gmt)
    # # Обыск во время исследования #
    #     if "тут есть что-то интересное" in gmt:
    #         event.research()
        
    # # Бой #    
    #     if "можно сразиться с ним" in gmt:
    #         event.fight()
    #     if "персонаж: " in gmt and "гильдия" not in gmt:
    #         event.fight_pvp()
    #     if "вероятно прикончивший хозяина" in gmt or "вышла на свет вашего костра" in gmt or "зато нашелся внезапный противник" in gmt:
    #         event.fight_start()

    # # Руины #
    #     if "начинаете обыск руин" in gmt:
    #         locaton_file_path = os.path.join(current_directory, "location.json")
    #         with open(locaton_file_path, 'r') as locaton_file:
    #             location = json.load(locaton_file)
    #         location["current"] = "ruins"
    #         with open(locaton_file_path, 'w') as locaton_file:
    #             json.dump(location, locaton_file, indent=4)
    #         if config["ruins"] == "off":
    #             return "Прервать поиск"
    #         else:
    #             print("wait")

    # # Охота #
    #     if "подготавливаетесь" in gmt:
    #         locaton_file_path = os.path.join(current_directory, "location.json")
    #         with open(locaton_file_path, 'r') as locaton_file:
    #             location = json.load(locaton_file)
    #         location["current"] = "hunt"
    #         with open(locaton_file_path, 'w') as locaton_file:
    #             json.dump(location, locaton_file, indent=4)
    #         if config["hunting"] == "off":
    #             return "Прервать охоту"
            
    # # Конец события #
    #     if any(phrase in gmt for phrase in hunt_end) or any(phrase in gmt for phrase in ruins_end):
    #         locaton_file_path = os.path.join(current_directory, "location.json")
    #         with open(locaton_file_path, 'r') as locaton_file:
    #             location = json.load(locaton_file)
    #         if location["current"] == "ruins":
    #             return "Прервать поиск"
    #         if location["current"] == "hunt":
    #             return "Прервать охоту"
        
    # # Завалы #    
    #     if "времени" in gmt and "повышение" in gmt:
    #         if config["stats"] == "on":
    #             minutes = nums_from_string.get_nums(gmt)[0]
    #             time.sleep((minutes + 5) * 60)
    #             return "Покинуть"
    #         if config["stats"] == "off":
    #             return "Покинуть"
    # # Ловушки #    
    #     if "благодаря ловкости и удаче" in gmt:
    #         return "Продoлжить"
    #     if "чтобы освободиться..." in gmt:
    #         return "Освободиться"

    # # Контр #
    #     if "уверены, что хотите совершить сделку" in gmt:
    #         if config['kontr'] == 'on':
    #             return "Продать трофеи"
    #         if config['kontr'] == 'off':
    #             return "Уйти"
    # # Горшочек с золотом #
    #     if "горш" in gmt and "вы замечаете" in gmt and "с золотом" in gmt:
    #         return "Продолжить"
    # # Сундук #
    #     if "добыча ожидает внутри" in gmt:
    #         return "Открыть"

    # # Останки #
    #     if "попробовать обыскать останки" in gmt:
    #         buttons = buttons.buttons_getter(vk_session)
    #         if stats['karma'] <= 18:
    #             if buttons[0][0] == "возложить цветы":
    #                 return "Возложить цветы"
    #             return "Уйти"
    #         if stats['karma'] > 18:
    #             return "Обыскать"  
            
    # # Целебный источник #
    #     if "с новыми силами" in gmt:
    #         return "Пpoдoлжить"
    # # Отшельник #
    #     if "выпадет от 4 до 6" in gmt:
    #         if config['hermit'] == 'on':
    #             return "Бросить кости"
    #         if config['hermit'] == 'off':    
    #             return "Уйти"

    # # Страницы #
    #     if "книгу целиком уже не спасти, но одна из страниц уцелела" in gmt:
    #         page = pages.answer_pages(gmt)
    #         return page
        
    # # Испытания # 
    #     if "для вставки какого-то небольшого предмета" in gmt:
    #         buttons = buttons.buttons_getter(vk_session)
    #         if buttons[0][0] == "открыть силой":
    #             return "Открыть силой"
    #         if config['trials'] == 'on':
    #             if buttons[0][0] == "вставить камень судьбы":
    #                 return "Вставить камень судьбы"
    #         if config['trials'] == 'off':
    #             return "Уйти"
    #     if "дверь с грохотом открывается" in gmt:
    #         trial = trials.answer_trails(gmt)
    #         for t in trial:
    #             message_sender.send_message(mess=t)
    #             time.sleep(2)
    #         return
    #     if "дверь не поддается вашим усилиям" in gmt:
    #         return "Уйти"

    # # Три двери #
    #     if "осталось только принять решение..." in gmt:
    #         doors = ["Правая", "Левая"]
    #         return random.choice(doors)
    #     if "за левой дверью..." in gmt:
    #         return "Открыть левую"
    #     if "за центральной дверью..." in gmt:
    #         return "Открыть центральную"
    #     if "за правой дверью..." in gmt:
    #         return "Открыть правую"
        
    # # Росток #
    #     if "земля вокруг выглядит очень сухой" in gmt:
    #         message_sender.send_message(mess="Хочу 1 воды", peer_id=585692525)
    #     if "1*первозданная вода:" in gmt:
    #         return "Полить растение"
    #     if "впитывать влагу" in gmt:
    #         return "Ждaть"
    #     if "вы вырастили и собрали" in gmt:
    #         return "Уйти"

    # # Кулдауны #
    #     if "летописец гильдии раз в сутки готов выдать вам случайную книгу навыков из своих запасов" in gmt:
    #         pass
    #     if "алхимик гильдии раз в сутки готов выдать вам полезный набор" in gmt:
    #         pass
    # # Новый уровень #
    #     if "скрытый проход на следующий уровень" in gmt:
    #         if config["lvlup"] == "on":
    #             return "Спуститься"
    #         if config["lvlup"] == "off":
    #             return "Остаться"

    # # Источник #
    #     if " отдыха: 1 час" in gmt:
    #         if config["istok"] == "off":
    #             return "Покинуть источник"
    #         if config["istok"] == "on":
    #             istok = 1  
    #             pass
    # # Пещера #
    #     if "можно попробовать угадать по одной букве" in gmt:        
    #         wonder.solve_wonder(longpoll, vk_session, session_api, gmt)
    #         return
        

    # # Лабиринт #
    #     if "ветер дует откуда" in gmt or "источник ветра совсем" in gmt or "ветер берет начало" in gmt:
    #         import maze
    #         # maze.solve_maze(gmt)
    #         message_sender.send_message("Покинуть лабиринт")
    #         time.sleep(2)
    #         return "Покинуть лабиринт"

    # # Развилка #
    #     if gmt != "" and "перед каждым проходом другими" in gmt:
    #         return crossroad.choose_path(gmt)

    def run(self) -> None:
        print("bot is running")
        from character import Character
        c = Character()
        c.update_stats()
        self.vk.listen_events(self.handle_event)