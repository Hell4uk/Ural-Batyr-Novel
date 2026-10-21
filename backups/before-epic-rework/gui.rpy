init offset = -2

init python:
    gui.init(1920, 1080)

define gui.accent_color = "#f2c879"
define gui.idle_color = "#e7e1d5"
define gui.idle_small_color = "#aeb9c8"
define gui.hover_color = "#fff1bd"
define gui.selected_color = "#e9ad52"
define gui.insensitive_color = "#778092"
define gui.muted_color = "#667184"
define gui.hover_muted_color = "#aab6c8"
define gui.text_color = "#f5f1e8"
define gui.interface_text_color = "#f5f1e8"

define gui.text_font = "fonts/Nunito.ttf"
define gui.name_text_font = "fonts/Nunito.ttf"
define gui.interface_text_font = "fonts/Nunito.ttf"
define gui.text_size = 34
define gui.name_text_size = 40
define gui.interface_text_size = 27
define gui.label_text_size = 32
define gui.notify_text_size = 24
define gui.title_text_size = 64

define gui.main_menu_background = "ural_art/cover.png"
define gui.game_menu_background = "ural_art/steppe.png"
define gui.textbox_height = 258
define gui.textbox_yalign = 1.0
define gui.name_xpos = 126
define gui.name_ypos = -12
define gui.name_xalign = 0.0
define gui.namebox_width = 420
define gui.namebox_height = 62
define gui.namebox_borders = Borders(22, 12, 22, 12)
define gui.namebox_tile = False
define gui.dialogue_xpos = 146
define gui.dialogue_ypos = 72
define gui.dialogue_width = 1620
define gui.dialogue_text_xalign = 0.0

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(14, 10, 14, 10)
define gui.button_tile = False
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0

define gui.choice_button_width = 1540
define gui.choice_button_height = None
define gui.choice_button_borders = Borders(24, 16, 24, 16)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = 29
define gui.choice_button_text_xalign = 0.0
define gui.choice_button_text_idle_color = "#f5f1e8"
define gui.choice_button_text_hover_color = "#fff1bd"
define gui.choice_button_text_insensitive_color = "#6e7685"

define gui.navigation_xpos = 92
define gui.choice_spacing = 14
define gui.navigation_spacing = 12
define gui.pref_spacing = 12
define gui.pref_button_spacing = 4
define gui.slot_spacing = 18
define gui.main_menu_text_xalign = 0.0
define gui.frame_borders = Borders(18, 18, 18, 18)
define gui.confirm_frame_borders = Borders(38, 38, 38, 38)
define gui.skip_ypos = 18
define gui.notify_ypos = 88
define gui.bar_size = 18
define gui.scrollbar_size = 14
define gui.slider_size = 20
define gui.bar_borders = Borders(8, 8, 8, 8)
define gui.scrollbar_borders = Borders(8, 8, 8, 8)
define gui.slider_borders = Borders(8, 8, 8, 8)
define gui.history_length = 250
define gui.history_height = 160
define gui.history_spacing = 10
define gui.nvl_borders = Borders(28, 28, 28, 28)
define gui.nvl_list_length = 6
define gui.nvl_height = None
define gui.nvl_spacing = 16
define gui.language = "unicode"

style default:
    properties gui.text_properties()
    language gui.language

style button:
    properties gui.button_properties("button")

style button_text:
    properties gui.text_properties("button")
    yalign 0.5

style frame:
    padding gui.frame_borders.padding
    background Solid("#101a27e8")

style bar:
    ysize gui.bar_size
    left_bar Solid("#e9ad52")
    right_bar Solid("#334052")

style vbar:
    xsize gui.bar_size
    top_bar Solid("#e9ad52")
    bottom_bar Solid("#334052")
