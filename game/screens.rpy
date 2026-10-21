```renpy
init python:
    config.overlay_screens.append("quick_menu")

screen say(who, what):
    window:
        id "window"
        style "dialogue_window"
        if who:
            text who id "who" style "speaker_name"
        text what id "what" style "dialogue_text"

style dialogue_window:
    background Solid("#0A1F12")
    xfill True
    ysize 310
    yalign 1.0
    padding (40, 22)

style speaker_name:
    xpos 110
    ypos 22
    xsize 1700
    size 34
    bold True
    color "#22C55E"

style dialogue_text:
    xpos 110
    ypos 77
    xsize 1700
    line_spacing 3
    adjust_spacing False

screen choice(items):
    zorder 20
    frame:
        align (0.5, 0.44)
        xsize 1500
        background Solid("#0A1F12")
        padding (24, 22)
        vbox:
            spacing 14
            for i in items:
                textbutton i.caption action i.action style "choice_button"

style choice_button is button:
    xfill True
    padding (26, 18)
    background Solid("#0A1F12")
    hover_background Solid("#22C55E")
    hover_color "#0A1F12"

style choice_button_text is button_text:
    size 30
    xalign 0.0
    color "#F1F5F9"
    hover_color "#F1F5F9"

screen story_hud():
    zorder 30
    if not _game_menu:
        frame:
            pos (40, 26)
            padding (20, 12)
            background Solid("#0A1F12")
            text "ПЕСНЬ [chapter] / 12  •  [chapter_title]" size 24 color "#22C55E"

        textbutton "Журнал  ·  J":
            pos (1640, 26)
            xsize 240
            action ShowMenu("journal")
            text_size 24
            text_color "#22C55E"
            background Solid("#0A1F12")
            hover_background Solid("#22C55E")
            hover_color "#0A1F12"

screen quick_menu():
    zorder 40
    if quick_menu and not main_menu and not _game_menu:
        hbox:
            align (0.5, 1.0)
            spacing 8
            textbutton "Назад" action Rollback() style "quick_button"
            textbutton "История" action ShowMenu("history") style "quick_button"
            textbutton "Пропуск" action Skip() style "quick_button"
            textbutton "Авто" action Preference("auto-forward", "toggle") style "quick_button"
            textbutton "Сохранить" action ShowMenu("save") style "quick_button"
            textbutton "Загрузить" action ShowMenu("load") style "quick_button"
            textbutton "Настройки" action ShowMenu("preferences") style "quick_button"

style quick_button is button:
    padding (15, 9)
    background None
    hover_background Solid("#22C55E")
    hover_color "#0A1F12"
    xmaximum 180

style quick_button_text is button_text:
    size 23
    color "#F1F5F9"
    hover_color "#F1F5F9"

screen navigation():
    vbox:
        spacing 12
        if main_menu:
            textbutton "Начать сказание" action Start() style "nav_button"
        else:
            textbutton "Продолжить" action Return() style "nav_button"
            textbutton "Сохранить" action ShowMenu("save") style "nav_button"
            textbutton "Журнал" action ShowMenu("journal") style "nav_button"
        textbutton "Загрузить" action ShowMenu("load") style "nav_button"
        textbutton "Настройки" action ShowMenu("preferences") style "nav_button"
        textbutton "Об игре" action ShowMenu("about") style "nav_button"
        if not main_menu:
            textbutton "Главное меню" action MainMenu() style "nav_button"
        textbutton "Выйти" action Quit(confirm=True) style "nav_button"

style nav_button is button:
    xsize 290
    yminimum 58
    background Solid("#0A1F12")
    hover_background Solid("#22C55E")

style nav_button_text is button_text:
    size 28
    color "#F1F5F9"
    hover_color "#F1F5F9"

screen main_menu():
    tag menu
    zorder 100
    add "menu landscape"
    add Solid("#0A1F12")
    frame:
        pos (100, 110)
        xysize (700, 860)
        padding (44, 36)
        vbox:
            spacing 18
            text "БАШКИРСКИЙ НАРОДНЫЙ ЭПОС" size 22 color "#22C55E"
            text "УРАЛ-БАТЫР" size 66 bold True color "#22C55E"
            text "Песнь живой воды" size 32
            null height 2
            text "Двенадцать песней о поисках бессмертия,\nиспытании силой и жизни ради других." size 25 line_spacing 5
            null height 10
            use navigation
            null height 10
            text "Художественная адаптация · 2.1" style "muted_text"
    text "Жизнь продолжается в добрых делах.":
        pos (1000, 900)
        size 30
        color "#F1F5F9"
        outlines [(2, "#0A1F12", 0, 0)]

screen game_menu(title):
    zorder 100
    add "menu landscape"
    add Solid("#0A1F12")
    frame:
        pos (60, 80)
        xysize (350, 920)
        padding (30, 32)
        vbox:
            spacing 24
            text "УРАЛ-БАТЫР" size 32 color "#22C55E" bold True
            use navigation
            null height 12
            textbutton "Назад  ·  Esc" action Return() style "nav_button"
    frame:
        pos (440, 80)
        xysize (1420, 920)
        padding (32, 30)
        text title size 42 color "#22C55E"
        viewport:
            pos (0, 88)
            xysize (1356, 750)
            scrollbars "vertical"
            mousewheel True
            draggable True
            side_yfill True
            transclude

screen save():
    tag menu
    zorder 100
    use file_slots("Сохранение", saving=True)

screen load():
    tag menu
    zorder 100
    use file_slots("Загрузка", saving=False)

screen file_slots(title, saving=False):
    use game_menu(title)
    vbox:
        spacing 24
        hbox:
            spacing 10
            textbutton "Авто" action FilePage("auto")
            textbutton "Быстрые" action FilePage("quick")
            for page in range(1, 5):
                textbutton "[page]" action FilePage(page)
        grid 3 2:
            spacing 18
            for slot in range(1, 7):
                button:
                    style "save_slot"
                    action (FileSave(slot) if saving else FileLoad(slot))
                    has vbox
                    spacing 8
                    add FileScreenshot(slot) xysize (384, 216)
                    text FileTime(slot, format="%d.%m.%Y  ·  %H:%M", empty="Пустой слот") size 24
                    text FileSaveName(slot) size 20 xmaximum 384 substitute False
    text "Сохранения прежнего короткого сюжета не загружайте в новое сказание." style "muted_text"

style save_slot is button:
    xysize (418, 326)
    padding (17, 14)
    background Solid("#0A1F12")
    hover_background Solid("#22C55E")

screen preferences():
    tag menu
    zorder 100
    use game_menu("Настройки")
    hbox:
        spacing 64
        vbox:
            xsize 600
            spacing 22
            text "Экран и чтение" style "panel_title"
            hbox:
                spacing 12
                textbutton "Окно" action Preference("display", "window")
                textbutton "Полный экран" action Preference("display", "fullscreen")
            text "Скорость появления текста" size 27
            bar id "text_speed" value Preference("text speed") xsize 570
            text "Справа — мгновенное отображение." style "muted_text"
            text "Пауза при авточтении" size 27
            bar id "auto_time" value Preference("auto-forward time") xsize 570
            textbutton "Крупный текст" action ToggleField(persistent, "large_text")
            textbutton "Уменьшить движение" action ToggleField(persistent, "reduced_motion")
            textbutton "Пропуск непрочитанного" action Preference("skip", "toggle")
        vbox:
            xsize 600
            spacing 22
            text "Звук" style "panel_title"
            text "Громкость музыки" size 27
            bar id "music_volume" value Preference("music volume") xsize 570
            textbutton "Выключить музыку":
                id "music_mute"
                action Preference("music mute", "toggle")
            text "Громкость эффектов" size 27
            bar id "sound_volume" value Preference("sound volume") xsize 570
            hbox:
                spacing 12
                textbutton "Выключить эффекты" action Preference("sound mute", "toggle")
                textbutton "Проверить" action Play("sound", "music/sfx/click.mp3")
            null height 10
            text "Золотым отмечена включённая настройка.\nНастройки сохраняются между запусками." style "muted_text"
            text "Space / Enter — далее\nEsc — меню\nJ — журнал\nH — скрыть интерфейс\nPage Up — вернуться к реплике" style "muted_text"

style panel_title:
    size 27
    color "#22C55E"
    bold True

screen history():
    tag menu
    zorder 100
    use game_menu("История диалогов")
    vbox:
        spacing 22
        if not _history_list:
            text "Здесь появятся прочитанные реплики." style "muted_text"
        for h in _history_list:
            vbox:
                xsize 1290
                spacing 6
                if h.who:
                    text h.who size 28 color "#22C55E" substitute False
                text h.what size 28 substitute False

screen journal():
    tag menu
    zorder 100
    use game_menu("Память пути")
    vbox:
        xsize 1280
        spacing 20
        text "Песнь [chapter]. [chapter_title]" style "panel_title"
        text "[objective]" size 28
        text "Смелость: [courage]    Милосердие: [mercy]    Рассудительность: [wisdom]" size 26
        text "Выборы меняют поступки и отклики героев. Основные события и завершение следуют эпосу." style "muted_text"
        null height 8
        for entry in journal_entries:
            text "— " + entry size 27
    key "j" action Return()

screen about():
    tag menu
    zorder 100
    use game_menu("Об игре и источниках")
    vbox:
        xsize 1280
        spacing 22
        text "Урал-батыр · Песнь живой воды" style "panel_title"
        text "Художественная адаптация башкирского народного эпоса в двенадцати песнях. Диалоги, переходы между сценами и игровые выборы написаны для игры; это не дословный текст эпоса." size 28
        text "Сюжет охватывает семью Янбирде и Янбике, освобождение Хумай, развилку братьев, царства Катила и Кахкахи, Самрау и Акбузата, войну с дивами, Яншишму и наследие сыновей." size 28
        text "Текст для сверки" style "panel_title"
        textbutton "Эпос «Урал-батыр»: академический перевод":
            action OpenURL("https://урал-батыр.рф/epos-ural-batyr-na-russkom-yazyke-aka/")
        text "Управление" style "panel_title"
        text "Enter / Space — далее; Esc — меню; J — журнал; H — скрыть интерфейс; Page Up — откат. Выборы доступны мышью и клавиатурой." size 27
        text "Версия [config.version]. Существующие изображения проекта используются как иллюстрации; они не являются этнографической реконструкцией." style "muted_text"

screen confirm(message, yes_action, no_action):
    modal True
    zorder 300
    add Solid("#0A1F12")
    frame:
        align (0.5, 0.5)
        xsize 1080
        padding (48, 42)
        vbox:
            spacing 32
            text message size 32 textalign 0.5 xalign 0.5 color "#F1F5F9"
            hbox:
                xalign 0.5
                spacing 30
                textbutton "Да" action yes_action xsize 180 text_xalign 0.5 style "confirm_button"
                textbutton "Нет" action no_action xsize 180 text_xalign 0.5 style "confirm_button"

style confirm_button is button:
    background Solid("#0A1F12")
    hover_background Solid("#22C55E")
    text_color "#F1F5F9"
    hover_text_color "#F1F5F9"
    padding (18, 10)

screen notify(message):
    zorder 250
    frame:
        align (0.5, 0.12)
        background Solid("#0A1F12")
        padding (20, 12)
        text message size 24 color "#22C55E"

screen skip_indicator():
    zorder 80
    frame:
        pos (42, 110)
        background Solid("#0A1F12")
        padding (20, 10)
        text "Пропуск…" size 22 color "#22C55E"

screen input(prompt):
    window:
        style "dialogue_window"
        vbox:
            pos (110, 30)
            spacing 18
            text prompt size 30 color "#F1F5F9"
            input id "input" size 32 length 80 color "#22C55E"

screen three_d_stage():
    zorder -10
    if persistent.reduced_motion:
        add "bg forest"
    else:
        add "bg forest" at landscape_drift
