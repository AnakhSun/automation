class Event():
    
    def __init__(self, text) -> None:
        self.text = text

    def process_location(self) -> str:
        return 

    def research(self) -> str:
        return "Обыскать"

    def time_event(self) -> str:
        return

    def fight(self) -> str:
        return
    
    def fight_start(self) -> str:
        return "В бой"

    def fight_pvp(self) -> str:
        return

    def ruins(self) -> str:
        return
    
    def hunt(self) -> str:
        return
    
    def lake(self) -> str:
        return

    def pages(self) -> str:

        pages = {
            "Грязный удар": "только в неожиданный момент, свободной от оружия рукой, в незащищенную зону...",
            "Гладиатор": "эти бойцы не носили, однако это позволяло полностью сосредоточиться на агрессии в бою, имея...",
            "Инициативность": "даже, казалось бы, всего одно умение, но именно оно может стать серьезным козырем...",
            "Прочность": "использовать особые пластины в доспехе, чтобы прикрыть эти места...",
            "Проклятие тьмы": "самое эффективное из них, позволяющее ослабить противника прямо во время...",
            "Мародер": "не брезговать осмотреть каждый карман, даже если с первого взгляда кажется, что...",
            "Рыбак": "обитают ближе ко дну, чаще скрываясь в водорослях...",
            "Воздаяние": "истинный путь, в зависимости от совершенных деяний и поступков...",
            "Дробящий удар": "более важен размах, который усилит тяжесть удара и позволит пробить...",
            "Охотник за головами": "выследить их можно по особым магическим знакам, которые оставляют только хранители...",
            "Расчётливость": "главное - точно соблюдать время между ними, и тогда появится возможность повторного...",
            "Быстрое восстановление": "поможет сэкономить время при перевязке, уменьшив...",
            "Регенерация": "если они небольшие - затянутся сами собой, даже в бою, не требуя дополнительного лечения...",
            "Устрашение": "такую позу, которая максимально подчеркнет опасность...",
            "Упорность": "падал, но снова вставал, продолжая путь к своей цели...",
            "Кровотечение": "не столько длина пореза, сколько его глубина...",
            "Подвижность": "своевременно и быстро совершенное - может спасти жизнь от любого, даже смертельного удара...",
            "Огонек надежды": "использовать собственный факел даже в том случае, если вокруг нет ни единого другого источника...",
            "Защитная стойка": "иногда важнее, чем атака. Переждав несколько ударов, можно восстановить...",
            "Целебный огонь": "но не стоит страшиться - ведь Вам, в отличие от противника, он не причинит вреда, а наоборот...",
            "Запасливость": "если связывать их в одну охапку, то они займут меньше места в...",
            "Суеверность": "и пусть эти приметы и не всегда будут полезны, но в случае, когда...",
            "Колющий удар": "прямой удар острием вперед. Лезвие должно войти достаточно...",
            "Слепота": "грязь под ногами, как самый простой вариант. Цельтесь в глаза, чтобы...",
            "Водохлеб": "позволит быстро откупорить крышку и одним глотком осушить...",
            "Режущий удар": "нанести удар вдоль, максимально сблизившись с противником, чтобы он точно не смог...",
            "Бесстрашие": "следить за каждым движением, которое может оказаться врагом, меньше обращая внимания на окружающее...",
            "Стойка сосредоточения": "отрешившись от внешнего мира, однако при этом не надейтесь избежать...",
            "Рассечение": "резким взмахом, едва задевая самым острием по широкому...",
            "Раскол": "в сочленение между пластинами, и только тогда они...",
            "Исследователь": "не обязательно настроены агрессивно, многих из них можно обойти просто...",
            "Заражение": "проникает в саму кровь врага, отравляя ее и не позволяя...",
            "Сила теней": "убедиться, что вокруг нет ни единого источника света, и собрать вокруг...",
            "Феникс": "переродиться из пепла, но только в том случае, если...",
            "Расправа": "будет достигнут только если противник находится при смерти, и уже не может...",
            "Неуязвимый": "не подставляя свои слабые точки под вероятную траекторию...",
            "Слабое исцеление": "жизненные силы вокруг себя и направить их поток в свое тело...",
            "Внимательность": "не только следить за всем, происходящим вокруг, но и не забывать о собственных карманах...",
            "Мощный удар": "и всю накопленную за это время силу высвободить в одном...",
            "Берсеркер": "и кровь, заливающая глаза, придаст силы и ярости для одного...",
            "Непоколебимый": "очистить разум от посторонних мыслей, сосредоточившись на...",
            "Удар вампира": "вонзить в плоть, незащищенную броней. Лучшей точкой является шея, если...",
            "Ошеломление": "резкий и громкий звук, который собьет концентрацию противника...",
            "Расторопность": "позволит быстрее перетаскивать камни, разбирая обвалившийся участок...",
            "Собиратель": "не всегда ценность находки может быть видна сразу, иногда приходится...",
            "Контратака": "и если провести удар прямо в этот момент, то противник попросту не успеет...",
            "Ведьмак": "спасительной жидкостью, которая, иногда, является полезнее любого заклинания...",
            "Ученик": "впитывать знания в любой ситуации, совершенствуя свои...",
            "Таран": "дополнительный вес, придающий силу удара вместе с разгоном...",
            "Браконьер": "разрезать вдоль, аккуратно поддев ножом внутреннюю часть...",
            "Картограф": "зарисовать на бумаге, каждый поворот, каждую...",
            "Ловкость рук": "выверенные движения позволят снять пробку быстрее и сократить время...",
            "Незаметность": "пригнувшись максимально мягко ступая по каменному...",
            "Устойчивость": "иммунитет организма, таким образом отравление не сможет...",
            "Атлетика": "правильно напрягая мышцы, чтобы позволить им...",
            "Парирование": "в нужный момент подставить свой клинок под удар, отведя...",
            "Знания Древних": "сама по себе, однако тайные знания, содержащиеся в...",
            "Угроза": "заставить противника призвать их для помощи в..."
        }

        text = text.split("...")[1]
        message = []
        for key in pages:        
            if text in pages[key].lower() or pages[key].lower() in text:
                message.append(key)
        return message
    
    def trials(self) -> str:
        return
    
    def smugger(self) -> str:
        return
    
    def pot(self) -> str:
        return
    
    def chest(self) -> str:
        return
    
    def dead_body(self) -> str:
        return
    
    def healing_spring(self) -> str:
        return
    
    def spring(self) -> str:
        return
    
    def three_doors(self) -> str:
        return
    
    def sprout(self) -> str:
        return
    
    def new_level(self) -> str:
        return
    
    def traps(self) -> str:
        return

    def maze(self) -> str:
        return

    def cave_of_wonders(self) -> str:
        return

    def crossroad(self) -> str:
        return
