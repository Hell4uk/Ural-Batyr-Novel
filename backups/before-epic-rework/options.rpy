init -1 python hide:
    config.has_autosave = True
    config.autosave_slots = 12
    config.window_title = "Урал-Батыр: Песнь живой воды"
    config.name = _("Урал-Батыр: Песнь живой воды")
    config.version = "2.0"
    config.window_icon = "ural_art/icon.png"
    config.save_directory = "UralBatyr-LivingWater-2"
    config.enter_transition = dissolve
    config.exit_transition = dissolve
    config.intra_transition = dissolve
    config.end_game_transition = dissolve
    config.window = "auto"

define gui.show_name = False
define gui.about = _("Интерактивная легенда о живой воде, доверии и выборе. Версия 2.0.")
define build.name = "UralBatyr-LivingWater"
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.main_menu_music = "music/main-menu-themse.ogg"
define config.check_conflicting_properties = True

default preferences.text_cps = 42
default preferences.afm_time = 15

init python:
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
