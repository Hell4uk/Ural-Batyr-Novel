init python:
    config.overlay_screens.append("quick_menu")

screen say(who, what):
    window:
        id "window"
        xalign 0.5
        yalign 1.0
        yoffset -64
        xsize 1500
        ysize 250
        background Solid("#0b2823ed")
        padding (36, 24)
        vbox:
            xfill True
            yfill True
            spacing 8
            if who:
                text who id "who" style "speaker_name" xfill True
            text what id "what" style "dialogue_text" size (int((36 if persistent.large_text else 32) * persistent.text_scale)) xfill True

style dialogue_window:
    background Solid("#0b2823ed")
    xalign 0.5
    xsize 1500
    ysize 250
    yalign 1.0
    padding (36, 24)

style speaker_name:
    xalign 0.0
    xsize 1188
    size 34
    bold True
    color "#afd9bb"

style dialogue_text:
    xalign 0.0
    xsize 1188
    line_spacing 4
    adjust_spacing False

screen choice(items):
    zorder 20
    frame:
        align (0.76, 0.56)
        xsize 660
        background Solid("#0b2823ed")
        padding (24, 24)
        vbox:
            spacing 12
            for i in items:
                textbutton i.caption action i.action style "choice_button" selected persistent.choice_highlight

screen preferences():
    tag menu
    zorder 100
    use game_menu("Настройки"):
        hbox:
            spacing 48
            vbox:
                xsize 620
                spacing 18
                text "Экран и чтение" style "panel_title"
                hbox:
                    spacing 10
                    textbutton "Окно" action Preference("display", "window") style "page_button"
                    textbutton "Полный экран" action Preference("display", "fullscreen") style "page_button"
                text "Скорость появления текста" size 24
                bar id "text_speed" value Preference("text speed") xsize 590
                text "Справа — мгновенное отображение." style "muted_text"
                text "Пауза при авточтении" size 24
                bar id "auto_time" value Preference("auto-forward time") xsize 590
                text "Размер текста диалогов" size 24
                bar value FieldValue(persistent, "text_scale", range=0.5, offset=0.75, step=0.05, style="slider", max_is_zero=False, force_step=True) xsize 590
                text "Текущий масштаб: [persistent.text_scale]" style "muted_text"
                textbutton "Крупный текст диалогов" action ToggleField(persistent, "large_text") selected persistent.large_text style "setting_button"
                textbutton "Уменьшить движение" action ToggleField(persistent, "reduced_motion") selected persistent.reduced_motion style "setting_button"
                textbutton "Подсветка выборов" action ToggleField(persistent, "choice_highlight") selected persistent.choice_highlight style "setting_button"
                textbutton "Пропускать непрочитанное" action Preference("skip", "toggle") style "setting_button"
            vbox:
                xsize 620
                spacing 18
                text "Звук" style "panel_title"
                text "Громкость музыки" size 24
                bar id "music_volume" value Preference("music volume") xsize 590
                textbutton "Выключить музыку" action Preference("music mute", "toggle") style "setting_button"
                text "Громкость эффектов" size 24
                bar id "sound_volume" value Preference("sound volume") xsize 590
                hbox:
                    spacing 10
                    textbutton "Выключить эффекты" action Preference("sound mute", "toggle") style "setting_button"
                    textbutton "Проверить" action Play("sound", "music/sfx/click.mp3") style "page_button"
                null height 8

style choice_button is button:
    xfill True
    padding (24, 18)
    background Solid("#15372fe8")
    hover_background Solid("#315748f2")
    selected_background Solid("#315748f2")

style choice_button_text is button_text:
    size 28
    xalign 0.0
    color "#e1ece3"
    hover_color "#ffffff"

screen story_hud():
    zorder 30
    if not main_menu:
        frame:
            pos (42, 34)
            padding (20, 12)
            background Solid("#0b2823d9")
            text "ПЕСНЬ [chapter] / 12  ·  [chapter_title]" size 23 color "#c0e2c8"

        textbutton "Журнал  ·  J" style "hud_button":
            pos (1640, 34)
            xsize 238
            action ShowMenu("journal")

style hud_button is button:
    padding (18, 12)
    background Solid("#0b2823d9")
    hover_background Solid("#315748f2")

style hud_button_text is button_text:
    size 23
    color "#e1ece3"
    hover_color "#ffffff"

screen quick_menu():
    zorder 40
    if quick_menu and not main_menu:
        hbox:
            align (0.5, 0.995)
            spacing 4
            textbutton "Назад" action Rollback() style "quick_button"
            textbutton "История" action ShowMenu("history") style "quick_button"
            textbutton "Пропуск" action Skip() style "quick_button"
            textbutton "Авто" action Preference("auto-forward", "toggle") style "quick_button"
            textbutton "Сохранить" action ShowMenu("save") style "quick_button"
            textbutton "Загрузить" action ShowMenu("load") style "quick_button"
            textbutton "Настройки" action ShowMenu("preferences") style "quick_button"

style quick_button is button:
    padding (14, 8)
    background Solid("#102f28d9")
    hover_background Solid("#315748f2")
    xmaximum 180

style quick_button_text is button_text:
    size 21
    color "#d5e4d9"
    hover_color "#ffffff"

screen navigation():
    vbox:
        spacing 10
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
    xfill True
    yminimum 56
    padding (20, 13)
    background Solid("#15372fd9")
    hover_background Solid("#315748f2")

style nav_button_text is button_text:
    size 25
    color "#e1ece3"
    hover_color "#ffffff"

screen main_menu():
    tag menu
    zorder 100
    add "menu landscape"
    add Solid("#071b18a8")
    frame:
        xalign 0.045
        yalign 0.5
        xsize 620
        ysize 850
        background Solid("#0b2823e8")
        padding (48, 42)
        vbox:
            spacing 15
            text "БАШКИРСКИЙ НАРОДНЫЙ ЭПОС" size 21 color "#a8cdb3"
            text "Урал-батыр" size 64 bold True color "#c2e5ca"
            text "Песнь живой воды" size 31 color "#e0e9e1"
            null height 5
            text "Двенадцать песен о поисках бессмертия,\nиспытании силы и жизни ради других." size 24 line_spacing 5 color "#d0ddd3"
            null height 10
            use navigation
            null height 4
            text "Художественная адаптация · 2.1" style "muted_text"
    text "Жизнь продолжается в добрых делах.":
        pos (1030, 920)
        size 27
        color "#e1ece3"
        outlines [(2, "#071b18", 0, 0)]

screen game_menu(title):
    zorder 100
    add "menu landscape"
    add Solid("#071b18b8")
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1844
        ysize 1016
        spacing 20
        frame:
            xsize 320
            yfill True
            background Solid("#0b2823e8")
            padding (24, 28)
            vbox:
                spacing 18
                text "Урал-батыр" size 30 color "#c2e5ca" bold True
                null height 4
                use navigation
                null height 8
                textbutton "Назад  ·  Esc" action Return() style "nav_button"
        frame:
            xfill True
            yfill True
            background Solid("#0b2823e8")
            padding (30, 26)
            vbox:
                xfill True
                yfill True
                spacing 18
                text title size 39 color "#c2e5ca"
                viewport:
                    xfill True
                    yfill True
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
    use game_menu(title):
        vbox:
            spacing 20
            hbox:
                spacing 8
                textbutton "Авто" action FilePage("auto") style "page_button"
                textbutton "Быстрые" action FilePage("quick") style "page_button"
                for page in range(1, 5):
                    textbutton "[page]" action FilePage(page) style "page_button"
            grid 3 2:
                xfill True
                spacing 16
                for slot in range(1, 7):
                    button:
                        style "save_slot"
                        action (FileSave(slot) if saving else FileLoad(slot))
                        has vbox
                        spacing 7
                        add FileScreenshot(slot) xysize (384, 216)
                        text FileTime(slot, format="%d.%m.%Y  ·  %H:%M", empty="Пустой слот") size 21
                        text FileSaveName(slot) size 19 xmaximum 384 substitute False
            text "Сохранения прежнего короткого сюжета не загружайте в новое сказание." style "muted_text"

style page_button is button:
    padding (16, 9)
    background Solid("#15372fd9")
    hover_background Solid("#315748f2")

style page_button_text is button_text:
    size 22
    color "#d5e4d9"
    hover_color "#ffffff"

style save_slot is button:
    xsize 418
    ysize 326
    padding (14, 12)
    background Solid("#102f28e8")
    hover_background Solid("#24483ce8")

style setting_button is button:
    padding (15, 10)
    background Solid("#15372fd9")
    hover_background Solid("#315748f2")
    selected_background Solid("#315748f2")

style setting_button_text is button_text:
    size 22
    color "#d5e4d9"
    hover_color "#ffffff"
    selected_color "#c2e5ca"

screen history():
    tag menu
    zorder 100
    use game_menu("История диалогов"):
        vbox:
            spacing 20
            if not _history_list:
                text "Здесь появятся прочитанные реплики." style "muted_text"
            for h in _history_list:
                vbox:
                    xsize 1290
                    spacing 6
                    if h.who:
                        text h.who size 25 color "#afd9bb" substitute False
                    text h.what size (32 if persistent.large_text else 27) substitute False

screen journal():
    tag menu
    zorder 100
    use game_menu("Память пути"):
        vbox:
            xsize 1280
            spacing 18
            text "Песнь [chapter]. [chapter_title]" style "panel_title"
            text "[objective]" size 26
            text "Смелость: [courage]    Милосердие: [mercy]    Рассудительность: [wisdom]" size 24
            text "Выборы меняют поступки и отклики героев. Основные события и завершение следуют эпосу." style "muted_text"
            null height 8
            for entry in journal_entries:
                text "— [entry]" size 25
    key "j" action Return()

screen about():
    tag menu
    zorder 100
    use game_menu("Об игре и источниках"):
        vbox:
            xsize 1280
            spacing 20
            text "Урал-батыр · Песнь живой воды" style "panel_title"
            text "Художественная адаптация башкирского народного эпоса в двенадцати песнях. Диалоги, переходы между сценами и игровые выборы написаны для игры; это не дословный текст эпоса." size 26
            text "Сюжет охватывает семью Янбирде и Янбике, освобождение Хумай, развилку братьев, царства Катила и Кахкахи, Самрау и Акбузата, войну с дивами, Яншишму и наследие сыновей." size 26
            null height 6
            text "Двенадцать песен" style "panel_title"
            for song_title, song_goal in songs:
                text "— [song_title]. [song_goal]" size 25
            null height 6
            text "Как влияют выборы" style "panel_title"
            text "Смелость отмечает поступки вопреки страху, милосердие — внимание к чужой беде, рассудительность — вопросы и осторожность. Черты открывают разные реплики и отклики героев, а финал следует эпосу." size 26
            text "Текст для сверки" style "panel_title"
            textbutton "Эпос «Урал-батыр»: академический перевод" action OpenURL("https://урал-батыр.рф/epos-ural-batyr-na-russkom-yazyke-aka/") style "page_button"
            text "Управление" style "panel_title"
            text "Enter / Space — далее; Esc — меню; J — журнал; H — скрыть интерфейс; Page Up — откат. Выборы доступны мышью и клавиатурой." size 25
            text "Версия [config.version]. Существующие изображения проекта используются как иллюстрации; они не являются этнографической реконструкцией." style "muted_text"

screen confirm(message, yes_action, no_action):
    modal True
    zorder 300
    add Solid("#061b18c9")
    frame:
        align (0.5, 0.5)
        xsize 900
        background Solid("#102f28f5")
        padding (42, 36)
        vbox:
            xfill True
            spacing 28
            text message size 30 textalign 0.5 xalign 0.5 color "#edf3ed" xfill True
            hbox:
                xalign 0.5
                spacing 24
                textbutton "Да" action yes_action xsize 170 text_xalign 0.5 style "confirm_button"
                textbutton "Нет" action no_action xsize 170 text_xalign 0.5 style "confirm_button"

style confirm_button is button:
    background Solid("#1a4035")
    hover_background Solid("#35614d")
    selected_background Solid("#35614d")
    padding (18, 10)

style confirm_button_text is button_text:
    size 24
    color "#edf3ed"
    hover_color "#ffffff"

screen notify(message):
    zorder 250
    frame:
        align (0.5, 0.12)
        background Solid("#102f28ed")
        padding (20, 12)
        text message size 23 color "#c2e5ca"

screen skip_indicator():
    zorder 80
    frame:
        pos (42, 110)
        background Solid("#102f28ed")
        padding (20, 10)
        text "Пропуск…" size 22 color "#c2e5ca"

screen input(prompt):
    window:
        style "dialogue_window"
        vbox:
            pos (0, 28)
            spacing 18
            text prompt size 28 color "#edf3ed"
            input id "input" size 30 length 80 color "#c2e5ca"

screen three_d_stage():
    zorder -10
    if persistent.reduced_motion:
        add "bg forest"
    else:
        add "bg forest" at landscape_drift

screen ending_card():
    modal True
    zorder 200
    add Solid("#071b18a8")
    frame:
        align (0.5, 0.5)
        xsize 900
        background Solid("#0b2823ed")
        padding (48, 42)
        vbox:
            xfill True
            spacing 24
            text "УРАЛ-БАТЫР" size 50 color "#c2e5ca" bold True xalign 0.5 textalign 0.5
            text "Сказание завершено" size 32 color "#edf3ed" xalign 0.5 textalign 0.5
            text "Художественная адаптация башкирского народного эпоса" size 24 color "#a8cdb3" xalign 0.5 textalign 0.5
            textbutton "Завершить" action Return() style "confirm_button" xalign 0.5
    key "dismiss" action Return()
