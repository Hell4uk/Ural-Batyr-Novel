# Original dialogue and scene writing based on the public-domain folk epic.
# See SOURCES.md for the editions used to check the sequence of events.
define n = Character(None)
define ur = Character("Урал", color="#edc47b")
define sh = Character("Шульген", color="#b8c9ed")
define hu = Character("Хумай", color="#bce3d5")
define father = Character("Янбирде", color="#ddc5a4")
define mother = Character("Янбике", color="#e7b6a5")
define katil = Character("Катил", color="#efa88b")
define zarkum = Character("Заркум", color="#bbd3a0")
define kahkaha = Character("Кахкаха", color="#bbd3a0")
define samrau = Character("Самрау", color="#b6dce6")
define azraka = Character("Азрака", color="#efa88b")
define elder = Character("Старец", color="#ddd2bc")
define algur = Character("Алгур", color="#c6d8bd")
define girl = Character("Дочь Катила", color="#e9c1ad")
define aihylu = Character("Айхылу", color="#c9d6f5")
define akbuzat = Character("Акбузат", color="#e4e8ee")
define son = Character("Идель", color="#b6dce6")

default chapter = 0
default chapter_title = "Начало пути"
default objective = "Узнать, что привело братьев на поиски Живого родника."
default courage = 0
default mercy = 0
default wisdom = 0
default journal_entries = []
default quick_menu = True
default rescued_people = False
default warned_zarkum = False
default trusted_brother = False
default remembered_elder = False
default ending_reached = False
default persistent.large_text = False
default persistent.reduced_motion = False
default persistent.text_scale = 1
default persistent.choice_highlight = True

init python:
    def bump_stat(stat, amount=1):
        setattr(store, stat, getattr(store, stat) + amount)
        names = {"courage": "Смелость", "mercy": "Милосердие", "wisdom": "Рассудительность"}
        renpy.notify("%s +1" % names.get(stat, stat))

    def reset_settings():
        persistent.large_text = False
        persistent.reduced_motion = False
        persistent.text_scale = 1
        persistent.choice_highlight = True
        renpy.notify("Настройки сброшены")

define songs = (
    ("Дом среди вод", "Выслушать Янбирде и понять, что значит запрет."),
    ("Лебедь и две дороги", "Освободить Хумай и отправиться вслед за её вестью."),
    ("Площадь Катила", "Помочь людям, которых обрекли на жертву."),
    ("Бык и власть", "Пройти испытание и освободить страну Катила."),
    ("Заркум и змеиное царство", "Не спутать благодарность с правом повелевать."),
    ("Дорога Шульгена", "Увидеть, как расходятся цели братьев."),
    ("У Самрау", "Встретить Хумай и узнать об Акбузате."),
    ("Небесный конь", "Выдержать испытание и принять ответственность за дар."),
    ("Обещание брата", "Решить, как ответить на просьбу Шульгена."),
    ("Война с дивами", "Защитить людей и противостоять Азраке."),
    ("Яншишма", "Понять, кому должна достаться живая вода."),
    ("Горы и реки", "Завершить путь Урала и передать его дело следующим поколениям."),
)

label splashscreen:
    return

label start:
    $ courage = 0
    $ mercy = 0
    $ wisdom = 0
    $ journal_entries = []
    $ rescued_people = False
    $ warned_zarkum = False
    $ trusted_brother = False
    $ remembered_elder = False
    $ ending_reached = False
    $ quick_menu = True
    stop music fadeout 1.0
    play music "music/backaudio/place_music4.ogg" fadein 2.0
    scene bg dawn with fade
    n "Это художественная адаптация башкирского народного эпоса. Игровые выборы и диалоги созданы для новеллы; основные события сохраняют путь Урал-батыра."
    jump epic_01

label song(number):
    hide screen story_hud
    window hide
    $ chapter = number
    $ chapter_title, objective = songs[number - 1]
    $ save_name = "Песнь %d. %s" % (chapter, chapter_title)
    centered "{size=26}УРАЛ-БАТЫР{/size}\n\n{size=48}{color=#edc47b}Песнь [chapter]. [chapter_title]{/color}{/size}"
    show screen story_hud
    return
