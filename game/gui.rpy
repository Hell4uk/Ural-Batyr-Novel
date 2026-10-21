init offset = -2
init python:
    gui.init(1920, 1080)

define gui.text_font = "fonts/Nunito.ttf"
define gui.name_text_font = "fonts/Nunito.ttf"
define gui.interface_text_font = "fonts/Nunito.ttf"
define gui.language = "unicode"
define gui.text_color = "#f4eee2"
define gui.interface_text_color = "#f4eee2"
define gui.accent_color = "#edc47b"
define gui.idle_color = "#d3dce2"
define gui.hover_color = "#ffffff"
define gui.selected_color = "#edc47b"
define gui.insensitive_color = "#73808c"
define gui.text_size = 32
define gui.name_text_size = 34
define gui.interface_text_size = 28
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = 28
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
    background Solid("#192c3be8")
    hover_background Solid("#304b60")
    selected_background Solid("#3b4c4b")
    insensitive_background Solid("#15202bcc")
    padding (18, 10)
style button_text:
    font gui.interface_text_font
    size 28
    color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color
    yalign 0.5
style frame:
    background Solid("#0d1927f2")
    padding (24, 24)
style bar:
    ysize 32
    left_bar Solid("#d8b471")
    right_bar Solid("#334b60")
    thumb Solid("#f6ebce", xsize=18, ysize=36)
    thumb_shadow None
    thumb_offset 0
style slider is bar
style scrollbar:
    ysize 12
    base_bar Solid("#203344")
    thumb Solid("#c7ae7c")
    unscrollable "hide"
style vscrollbar:
    xsize 12
    base_bar Solid("#203344")
    thumb Solid("#c7ae7c")
    unscrollable "hide"
style panel_title:
    size 30
    color gui.accent_color
    bold True
style muted_text:
    size 24
    color "#b4c0cb"
