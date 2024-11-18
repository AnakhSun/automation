from config import Config
import requests

class Character:
    def __init__(self):
        self.level = None
        self.prime_status = None
        self.hp = None
        self.max_hp = None
        self.traumas = None
        self.free_space = None
        self.karma = None
        self.masks = None
        self.active_masks = None
        self.hunger = None
        self.location = None
        self.pointed_location = None
        self.gold = None
        self.shards = None
        self.fish_trophies = None
        self.trophies = None
        self.elit_trophies = None
        self.fish = None
        self.meat = None
        self.strength = None
        self.dexterity = None
        self.endurance = None
        self.attack = None
        self.armor = None
        self.defense = None
        self.accuracy = None
        self.concentration = None
        self.evasion = None
        self.all_potions = None
        self.healing_potions = None
        self.poisons_potions = None
        self.accuracy_potions = None
        self.trauma_potions = None
        self.second_action_type = None
        self.second_action = None
        self.stand = None
        self.active_books = []
        self.books = []
        self.fast_fight = None
        self.loud_roar = None
        self.is_escapable = None
        self.dot_hot = None

        self.cooldown_tavern = None
        self.cooldown_guild_book = None
        self.cooldown_guild_potion = None
        self.cooldown_garden = None
        self.garden_level = None


    def make_url(self, mode: str, item_id = None):
        print(mode)
        url = None
        if mode == "profile":
            url = (
                f'https://vip3.activeusers.ru/app.php?act=user'
                f'&auth_key={Config.VIP3_TOKEN}'
                f'&viewer_id={Config.VIEWER_ID}'
                f'&group_id={Config.GROUP_ID}'
                f'&api_id={Config.API_ID}'
            )
        if mode == "stats":
            url = (
                f'https://vip3.activeusers.ru/app.php?act=pages&id=699'
                f'&auth_key={Config.VIP3_TOKEN}'
                f'&viewer_id={Config.VIEWER_ID}'
                f'&group_id={Config.GROUP_ID}'
                f'&api_id={Config.API_ID}'
            )
        if mode == "item":
            url = (
                f"https://vip3.activeusers.ru/app.php"
                f"?act=item&id={item_id}"
                f"&auth_key={Config.VIP3_TOKEN}"
                f"&viewer_id={Config.VIEWER_ID}"
                f"&group_id={Config.GROUP_ID}"
                f"&api_id={Config.API_ID}"
            )

        return url


    def update_stats(self) -> None:
        url_profile = self.make_url(mode="profile")
        url_stats = self.make_url(mode="stats")
        response_profile = requests.get(url_profile)

        selectors_profile = {
            'level': '#app_content > div.container > div > div.row > div > div > div > div.portlet-body.money-list > div:nth-child(1) > div:nth-child(1) > div > span.money-list-rescount',
            'attack': '#app_content > div.container > div > div.row > div > div > div > div.portlet-body.money-list > div:nth-child(1) > div:nth-child(2) > div > span.money-list-rescount',
            'armor': '#app_content > div.container > div > div.row > div > div > div > div.portlet-body.money-list > div:nth-child(1) > div:nth-child(3) > div > span.money-list-rescount',
            'strength': '#app_content > div.container > div > div.row > div > div > div > div.portlet-body.money-list > div:nth-child(2) > div:nth-child(1) > div > span.money-list-rescount',
            'dexterity': '#app_content > div.container > div > div.row > div > div > div > div.portlet-body.money-list > div:nth-child(2) > div:nth-child(2) > div > span.money-list-rescount',
            'endurance': '#app_content > div.container > div > div.row > div > div > div > div.portlet-body.money-list > div:nth-child(2) > div:nth-child(2) > div > span.money-list-rescount',
            'gold': '#r_13322 > span',
            'free_space': '#r_13344 > span',
            'trophies': '#r_13500 > span',
            'elit_trophies': '#r_14483 > span',
            'meat': '#r_14976 > span',
            'fish': '#r_15027 > span',
            'traumas': '#r_13452 > span:nth-child(1)',
            'poisons': '#r_14609 > span:nth-child(1)'
        }


        selectors_page = {
            'karma': '.element > p:nth-child(8)',
            'hungry': '.element > p:nth-child(9)'
        }


        # response_stats = requests.get(url_stats)
        