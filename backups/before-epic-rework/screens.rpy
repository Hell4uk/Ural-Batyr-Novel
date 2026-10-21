# Чистый интерфейс проекта: контрастные панели, крупные зоны клика и один набор стилей.

style panel:
    background Solid("#0b1525d9")
    padding (28, 22)

style panel_title:
    color "#f2c879"
    size 24
    bold True

style hud_text:
    color "#e9eef5"
    size 22

screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        background Solid("#08111ddd")
        ysize gui.textbox_height
        yalign 1.0
        if who is not None:
            frame:
                style "namebox"
                text who id "who"
        text what id "what"

style namebox:
    xpos gui.name_xpos
    ypos gui.name_ypos
    xsize gui.namebox_width
    ysize gui.namebox_height
    background Solid("#1b3146f5")
    padding gui.namebox_borders.padding

style say_label:
    color "#f2c879"
    size gui.name_text_size
    bold True
    xalign 0.0
    yalign 0.5

style say_dialogue:
    color "#f5f1e8"
    size gui.text_size
    xpos gui.dialogue_xpos
    ypos gui.dialogue_ypos
    xsize gui.dialogue_width
    line_spacing 4

screen choice(items):
    style_prefix "choice"
    vbox:
        xalign 0.5
        yalign 0.55
        spacing gui.choice_spacing
        for i in items:
            textbutton i.caption action i.action

style choice_button:
    xsize gui.choice_button_width
    background Frame(Solid("#101c2ddd"), 18, 18)
    hover_background Frame(Solid("#26465eef"), 18, 18)
    insensitive_background Frame(Solid("#10151ddd"), 18, 18)
    padding gui.choice_button_borders.padding

style choice_button_text:
    color "#f5f1e8"
    hover_color "#fff1bd"
    size gui.choice_button_text_size
    xalign 0.0

screen three_d_stage():
    # Три независимых слоя с разной скоростью движения имитируют перспективу.
    zorder -10
    add "bg sky" at stage_sky
    add Crop((0, 210, 1600, 690), "bg mountains") at stage_mountains
    add Crop((0, 395, 1600, 505), "bg forest") at stage_forest
    add Solid("#07111b22")
    text "✦" at float_spark(0.0, 0.18, 0.62) size 18 color "#f2c879"
    text "✦" at float_spark(1.4, 0.71, 0.53) size 14 color "#b7e0d4"
    text "✦" at float_spark(2.3, 0.84, 0.74) size 20 color "#f2c879"

screen story_hud():
    zorder 50
    frame:
        style "panel"
        xalign 0.03
        yalign 0.035
        xsize 430
        vbox:
            spacing 8
            text "УРАЛ-БАТЫР  •  ГЛАВА [chapter]" style "panel_title"
            text "Путь: [route_name]" style "hud_text"
            hbox:
                spacing 22
                text "Храбрость [courage]" style "hud_text"
                text "Милосердие [mercy]" style "hud_text"
            hbox:
                spacing 22
                text "Мудрость [wisdom]" style "hud_text"
                text "Доверие [humay_trust]" style "hud_text"
    hbox:
        xalign 0.97
        yalign 0.035
        spacing 10
        textbutton "ЖУРНАЛ  J" action Show("journal") style "hud_button"
        textbutton "МЕНЮ  Esc" action ShowMenu() style "hud_button"
    key "j" action Show("journal")

style hud_button:
    background Solid("#101c2ddd")
    hover_background Solid("#26465eef")
    padding (18, 12)
style hud_button_text:
    size 20
    color "#e9eef5"
    hover_color "#fff1bd"

screen journal():
    modal True
    zorder 200
    add Solid("#050a12dd")
    frame:
        style "panel"
        xalign 0.5
        yalign 0.5
        xsize 1080
        ysize 720
        vbox:
            spacing 16
            text "ПОЛЕВОЙ ЖУРНАЛ" style "panel_title"
            text "Состояние экспедиции" size 22 color "#aeb9c8"
            null height 8
            text "Осколки источника: [source_shards] / 3" style "hud_text"
            text "Спутники: [companions]" style "hud_text"
            text "Репутация у Хумай: [humay_trust]" style "hud_text"
            null height 10
            text "Цель" style "panel_title"
            text "Найти живую воду в горах Ирем и вернуть её в долину до первой грозы. Каждый выбор меняет путь, союзников и финал." style "hud_text"
            null height 20
            textbutton "Закрыть  (J / Esc)" action Hide("journal") style "hud_button"
    key "j" action Hide("journal")
    key "K_ESCAPE" action Hide("journal")

screen route_map():
    modal True
    zorder 150
    add Solid("#050a12dd")
    frame:
        style "panel"
        xalign 0.5
        yalign 0.5
        xsize 1220
        ysize 650
        vbox:
            spacing 16
            text "КАРТА ПЕРЕВАЛА" style "panel_title"
            text "След Хумай расходится у старого камня. Выбери первый риск." style "hud_text"
            null height 8
            hbox:
                spacing 18
                textbutton "Лесные тропы\nтише, но длиннее" action Return("forest") style "map_button"
                textbutton "Каменный кряж\nкороче, но опаснее" action Return("ridge") style "map_button"
                textbutton "Озёрная низина\nбыстрый шанс найти воду" action Return("lake") style "map_button"

style map_button:
    xsize 350
    ysize 180
    background Solid("#172a3dde")
    hover_background Solid("#2c5367ee")
    padding (24, 22)
style map_button_text:
    size 24
    color "#f5f1e8"
    hover_color "#fff1bd"
    textalign 0.5

screen navigation():
    vbox:
        xalign 0.08
        yalign 0.5
        spacing 8
        textbutton "Продолжить" action ShowMenu("load") style "menu_button"
        textbutton "Новая история" action Start() style "menu_button"
        textbutton "Сохранить" action ShowMenu("save") style "menu_button"
        textbutton "Загрузить" action ShowMenu("load") style "menu_button"
        textbutton "Настройки" action ShowMenu("preferences") style "menu_button"
        textbutton "Выйти" action Quit(confirm=True) style "menu_button"

style menu_button:
    xsize 400
    background Solid("#101c2db8")
    hover_background Solid("#2a4b64e8")
    padding (22, 13)
style menu_button_text:
    size 28
    color "#f5f1e8"
    hover_color "#fff1bd"

screen main_menu():
    tag menu
    add "ural_art/cover.png"
    add Solid("#07111b55")
    frame:
        background Solid("#07111bcc")
        xalign 0.07
        yalign 0.17
        xsize 610
        ysize 680
        padding (48, 42)
        vbox:
            spacing 18
            text "УРАЛ-БАТЫР" size 64 color "#f2c879" bold True
            text "ПЕСНЬ ЖИВОЙ ВОДЫ" size 27 color "#b7e0d4" bold True
            null height 18
            text "Интерактивная легенда о двух братьях, которые идут за источником сквозь степь, лес и собственные страхи." size 25 color "#e9eef5" line_spacing 5
            null height 30
            use navigation
            null height 18
            text "Версия 2.0  •  21 октября 2026" size 17 color "#9aa8ba"

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    tag menu
    add "ural_art/steppe.png"
    add Solid("#07111bcc")
    frame:
        style "panel"
        xalign 0.5
        yalign 0.5
        xsize 1500
        ysize 820
        vbox:
            text title size 38 color "#f2c879"
            null height 14
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                ymaximum 670
                transclude
            textbutton "Назад" action Return() style "hud_button"

screen save():
    tag menu
    use game_menu("СОХРАНИТЬ ИГРУ"):
        grid 3 2:
            spacing 18
            for slot in range(1, 7):
                textbutton "Слот [slot]" action FileSave(slot) style "slot_button"

screen load():
    tag menu
    use game_menu("ЗАГРУЗИТЬ ИГРУ"):
        grid 3 2:
            spacing 18
            for slot in range(1, 7):
                textbutton "Слот [slot]" action FileLoad(slot) style "slot_button"

style slot_button:
    xsize 380
    ysize 110
    background Solid("#172a3dde")
    hover_background Solid("#2c5367ee")
    padding (20, 16)
style slot_button_text:
    size 25
    color "#f5f1e8"
    hover_color "#fff1bd"

screen preferences():
    tag menu
    use game_menu("НАСТРОЙКИ"):
        vbox:
            spacing 14
            text "Экран" style "panel_title"
            textbutton "Оконный режим" action Preference("display", "window") style "slot_button"
            textbutton "Полный экран" action Preference("display", "fullscreen") style "slot_button"
            text "Звук" style "panel_title"
            textbutton "Музыка: вкл / выкл" action Preference("music mute", "toggle") style "slot_button"
            textbutton "Звуки: вкл / выкл" action Preference("sound mute", "toggle") style "slot_button"

screen history():
    tag menu
    use game_menu("ИСТОРИЯ ДИАЛОГОВ"):
        vbox:
            spacing 12
            for h in _history_list:
                if h.who:
                    text "[h.who]: [h.what]" style "hud_text"
                else:
                    text h.what style "hud_text"

screen confirm(message, yes_action, no_action):
    modal True
    add Solid("#050a12e8")
    frame:
        style "panel"
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 20
            text message style "hud_text"
            hbox:
                spacing 18
                textbutton "Да" action yes_action style "hud_button"
                textbutton "Нет" action no_action style "hud_button"
    key "game_menu" action no_action

screen notify(message):
    frame:
        background Solid("#101c2df0")
        xalign 0.5
        yalign 0.12
        padding (24, 14)
        text message color "#f5f1e8" size 22
    timer 3.0 action Hide("notify")

screen quick_menu():
    zorder 100
    hbox:
        xalign 0.5
        yalign 0.985
        spacing 8
        textbutton "Назад" action Rollback() style "quick_button"
        textbutton "История" action ShowMenu("history") style "quick_button"
        textbutton "Авто" action Preference("auto-forward", "toggle") style "quick_button"
        textbutton "Сохранить" action ShowMenu("save") style "quick_button"
        textbutton "Настройки" action ShowMenu("preferences") style "quick_button"

style quick_button:
    background Solid("#0b1525c0")
    hover_background Solid("#26465ed9")
    padding (13, 8)
style quick_button_text:
    size 19
    color "#c7d0dc"
    hover_color "#fff1bd"
