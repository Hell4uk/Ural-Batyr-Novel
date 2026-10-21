define n = Character(None, what_color="#f5f1e8")
define ur = Character("Урал", color="#f2c879")
define sh = Character("Шульген", color="#e5a4a3")
define hu = Character("Хумай", color="#b7e0d4")
define sa = Character("Сауле", color="#9fc5e8")
define kh = Character("Карахан", color="#e8a578")
define spirit = Character("Голос источника", color="#bcd5ff")

default chapter = 0
default route_name = "не выбран"
default courage = 0
default mercy = 0
default wisdom = 0
default humay_trust = 0
default brotherhood = 0
default source_shards = 0
default companions = "Шульген"
default storm_clock = 0
default spared_karahan = False
default learned_lesson = False

label splashscreen:
    return

label start:
    $ chapter = 0
    $ route_name = "рассветный путь"
    $ courage = 0
    $ mercy = 0
    $ wisdom = 0
    $ humay_trust = 0
    $ brotherhood = 0
    $ source_shards = 0
    $ companions = "Шульген"
    $ storm_clock = 0
    $ spared_karahan = False
    $ learned_lesson = False
    jump prologue

label prologue:
    scene bg dawn with fade
    show screen story_hud
    $ chapter = 1
    centered "{size=46}{color=#f2c879}УРАЛ-БАТЫР{/color}{/size}\n{size=25}ПЕСНЬ ЖИВОЙ ВОДЫ{/size}\n\n{size=20}Интерактивная легенда о выборе и возвращении{/size}"
    show screen story_hud
    n "В год, когда река отступила от камней, в долине осталось три колодца и одна надежда. На рассвете Урал заметил на горизонте голубой отблеск: так сияет вода, если она ещё помнит своё имя."
    show ural at center_character with dissolve
    ur "Отец говорил: источник не прячется от смелых. Он прячется от тех, кто приходит брать."
    show shulgen at right_character with dissolve
    sh "А Карахан уже собрал людей у северного перевала. Если мы опоздаем, он запечатает воду для себя."
    n "В дорогу можно было взять только один талисман — кремень, чашу или карту звёзд."
    menu:
        "Взять кремень: огонь для тех, кто замёрзнет.":
            $ courage += 1
            $ route_name = "огненный след"
            ur "Пламя видно издалека. Пусть оно станет обещанием, а не оружием."
        "Взять чашу: воду делят до последней капли.":
            $ mercy += 1
            $ humay_trust += 1
            $ route_name = "чаша доверия"
            ur "Пустая чаша — не слабость. Это место для того, что мы найдём."
        "Взять карту звёзд: сначала понять путь.":
            $ wisdom += 1
            $ route_name = "звёздная тропа"
            ur "Кто знает направление, тот не спорит с ветром."
    jump chapter_one

label chapter_one:
    $ chapter = 2
    scene bg steppe with dissolve
    n "К полудню братья встретили девушку с медным компасом. Сауле искала тот же источник, но её караван рассыпался в песчаной буре."
    show saule at left_character with dissolve
    sa "Я видела три следа на плато. Один ведёт к воде, два — к тем, кто хочет, чтобы мы поверили в воду."
    show shulgen at right_character with dissolve
    sh "Слишком много загадок для одного дня."
    menu:
        "Позвать Сауле с собой и поделиться припасами.":
            $ mercy += 1
            $ brotherhood += 1
            $ companions = "Шульген, Сауле"
            sa "Тогда мой компас — общий."
            ur "И наша ответственность тоже."
        "Попросить её вести, но оставить запасы братьям.":
            $ wisdom += 1
            $ companions = "Шульген, Сауле"
            sa "Честная сделка. Только не удивляйся, если путь тоже попросит плату."
        "Идти дальше одному отряду.":
            $ courage += 1
            sh "Ты умеешь быть смелым, но иногда смелость — это открыть дверь."
    jump chapter_two

label chapter_two:
    $ chapter = 3
    scene bg forest with dissolve
    n "В еловом лесу воздух стал прохладным, а шаги — тише. Между деревьями вспыхнули три светлых осколка: память источника, расколотая давней засухой."
    show humay at center_character with dissolve
    hu "Осколки откликаются на поступки. Сила не в том, чтобы собрать их любой ценой."
    hide humay
    show screen three_d_stage
    $ path = renpy.call_screen("route_map")
    if path == "forest":
        $ route_name = "тихие тропы"
        $ wisdom += 1
        $ source_shards += 1
        n "Вы обошли ловушку по мху и нашли первый осколок под корнями старой ели."
    elif path == "ridge":
        $ route_name = "каменный кряж"
        $ courage += 1
        $ source_shards += 1
        n "Шульген удержал осыпь, а Урал вытащил осколок из трещины. Страх остался позади, но ладони дрожали."
    else:
        $ route_name = "озёрная низина"
        $ mercy += 1
        $ humay_trust += 1
        $ source_shards += 1
        n "У озера вы напоили раненую лань. Вода ответила кругами — и осколок поднялся сам."
    jump chapter_three

label chapter_three:
    $ chapter = 4
    hide screen three_d_stage
    scene bg storm with dissolve
    $ storm_clock += 1
    n "К вечеру поднялась гроза. На перевале Карахан поставил сторожевые костры и предложил сделку: карта источника в обмен на молчание."
    show ural at left_character with dissolve
    show shulgen at right_character with dissolve
    kh "Вода принадлежит тому, кто первым добрался до неё. Уйдите — и долина проживёт ещё одну зиму."
    menu:
        "Объединить людей Карахана с долиной.":
            $ mercy += 1
            $ humay_trust += 1
            $ brotherhood += 1
            $ spared_karahan = True
            kh "Ты предлагаешь мне не власть, а работу. Это опаснее, чем меч."
        "Вызвать Карахана на честный поединок.":
            $ courage += 2
            $ spared_karahan = False
            kh "Пусть источник рассудит нас."
        "Сделать вид, что согласен, и ночью забрать карту.":
            $ wisdom += 2
            $ spared_karahan = True
            sh "Хитрость спасает день. Но что она спасёт в тебе?"
    jump chapter_four

label chapter_four:
    $ chapter = 5
    scene bg cave with dissolve
    n "За водопадом открылась пещера. Здесь не было сундуков — только круглый камень, три углубления и голос, похожий на дождь по крыше."
    spirit "Назови цену воды."
    menu:
        "Цена — память: каждый расскажет, чего боится.":
            $ wisdom += 1
            $ humay_trust += 1
            $ learned_lesson = True
            ur "Я боюсь стать сильным так, чтобы перестать слышать других."
            sh "Я боюсь, что брат однажды уйдёт вперёд и не оглянётся."
        "Цена — сила: я подниму камень один.":
            $ courage += 1
            $ learned_lesson = False
            ur "Пусть мои руки докажут, что я достоин дороги."
        "Цена — выбор: источник должен решать сам.":
            $ mercy += 2
            $ learned_lesson = True
            ur "Вода не чья-то добыча. Мы лишь возвращаем ей дорогу."
    $ source_shards += 2
    jump finale

label finale:
    $ chapter = 6
    scene bg spring with fade
    hide screen three_d_stage
    n "Утром вода вышла из камня тонкой серебряной нитью. Она не затопила долину — она нашла старое русло, которое люди забыли."
    if source_shards >= 3 and humay_trust >= 2 and learned_lesson:
        jump ending_spring
    elif courage >= 2 and brotherhood >= 1:
        jump ending_fire
    else:
        jump ending_wanderer

label ending_spring:
    show humay at center_character with dissolve
    hu "Источник жив, потому что вы не пытались стать его хозяевами."
    n "Долина получила воду, а Карахан — место за общим столом. Сауле нанесла новый путь на карту, и впервые за много лет её линия не заканчивалась крестом."
    centered "{size=42}{color=#b7e0d4}ФИНАЛ: САД НА КАМНЕ{/color}{/size}\n\nВы вернули воде свободу и нашли союзников."
    hide screen story_hud
    return

label ending_fire:
    scene bg dawn with fade
    n "Вы открыли русло силой и успели до грозы. Вода пришла, но часть осколков осталась в пещере — вместе с вопросами, на которые ещё предстоит ответить."
    centered "{size=42}{color=#f2c879}ФИНАЛ: ДОРОГА ОГНЯ{/color}{/size}\n\nСмелость спасла долину. Теперь ей нужны мудрость и время."
    hide screen story_hud
    return

label ending_wanderer:
    scene bg mountains with fade
    n "Источник показал дорогу, но не открылся полностью. Урал продолжил путь с чашей, картой и людьми, которым ещё нужно научиться доверять друг другу."
    centered "{size=42}{color=#9fc5e8}ФИНАЛ: НЕОКОНЧЕННАЯ ПЕСНЬ{/color}{/size}\n\nИстория продолжается там, где выбор становится привычкой."
    hide screen story_hud
    return
