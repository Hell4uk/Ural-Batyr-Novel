init offset = -2
init python:
    gui.init(1920, 1080)

define gui.text_font = "fonts/Nunito.ttf"
define gui.name_text_font = "fonts/Nunito.ttf"
define gui.interface_text_font = "fonts/Nunito.ttf"
define gui.language = "unicode"
define gui.text_color = "#edf3ed"
define gui.interface_text_color = "#edf3ed"
define gui.accent_color = "#b8dfc2"
define gui.idle_color = "#d5e4d9"
define gui.hover_color = "#ffffff"
define gui.selected_color = "#b8dfc2"
define gui.insensitive_color = "#84988c"
define gui.text_size = 32
define gui.name_text_size = 34
define gui.interface_text_size = 26
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = 26
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(18, 10, 18, 10)
define gui.button_tile = False
define config.thumbnail_width = 384
define config.thumbnail_height = 216
define config.history_length = 250

style default:
    font gui.text_font
    size gui.text_size
    color gui.text_color
    language gui.language
style button:
    background Solid("#15372fd9")
    hover_background Solid("#315748f2")
    selected_background Solid("#315748f2")
    insensitive_background Solid("#10261fcc")
    padding (20, 12)
style button_text:
    font gui.interface_text_font
    size gui.button_text_size
    color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color
    yalign 0.5
style frame:
    background Solid("#0b2823ed")
    padding (24, 24)
style bar:
    ysize 32
    left_bar Solid("#8fbea0")
    right_bar Solid("#294a3f")
    thumb Solid("#d7ecdc", xsize=18, ysize=36)
    thumb_shadow None
    thumb_offset 0
style slider is bar
style scrollbar:
    ysize 12
    base_bar Solid("#203f35")
    thumb Solid("#a7cfb3")
    unscrollable "hide"
style vscrollbar:
    xsize 12
    base_bar Solid("#203f35")
    thumb Solid("#a7cfb3")
    unscrollable "hide"
style panel_title:
    size 30
    color gui.accent_color
    bold True
style muted_text:
    size 26
    color "#c3d4c6"
