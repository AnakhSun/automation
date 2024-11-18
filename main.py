from fight_analyser import FightAnalyser
from bot import Bot
from multiprocessing import Process

def run_bot() -> None:
    bot = Bot()
    bot.run()

def run_fight_analyser() -> None:
    fightanalyser = FightAnalyser()
    fightanalyser.run()

def main() -> None:
    bot_process = Process(target=run_bot)
    fight_analyser_process = Process(target=run_fight_analyser)
    
    bot_process.start()
    fight_analyser_process.start()
    
    bot_process.join()
    fight_analyser_process.join()

if __name__ == "__main__":
    main()


