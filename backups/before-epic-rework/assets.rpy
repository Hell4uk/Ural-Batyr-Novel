# Единая карта ресурсов. Все пути относительные к папке game.

image bg steppe = "ural_art/steppe.jpg"
image bg cave = "ural_art/cave.jpg"
image bg mountains = "ural_art/mountains.jpeg"
image bg forest = "ural_art/forest.jpg"
image bg settlement = "ural_art/settlement.jpg"
image bg storm = "ural_art/storm.jpg"
image bg sky = "ural_art/sky.jpg"
image bg underworld = "ural_art/underworld.jpg"
image bg spring = "ural_art/spring.jpg"
image bg battle = "ural_art/battle.jpg"
image bg dawn = "ural_art/dawn.jpg"

image ural = "images/Uto/uto_default.png"
image shulgen = "images/Michi/michi_default.png"
image humay = "images/Akiko/akiko_default.png"
image saule = "images/Akiko/akiko smile.png"

transform center_character:
    xalign 0.5
    yalign 0.95
    zoom 0.72

transform left_character:
    xalign 0.22
    yalign 0.95
    zoom 0.64

transform right_character:
    xalign 0.78
    yalign 0.95
    zoom 0.64

# Панорамирование слоёв создаёт ощущение объёма без тяжёлого 3D-движка.
transform stage_sky:
    xalign 0.5
    yalign 0.5
    zoom 1.04
    linear 18.0 xoffset 18
    linear 18.0 xoffset -18
    repeat

transform stage_mountains:
    xalign 0.5
    yalign 1.0
    zoom 1.10
    linear 12.0 xoffset -28
    linear 12.0 xoffset 28
    repeat

transform stage_forest:
    xalign 0.5
    yalign 1.0
    zoom 1.20
    linear 8.0 xoffset 42
    linear 8.0 xoffset -42
    repeat

transform float_spark(delay, x, y):
    xpos x
    ypos y
    alpha 0.0
    pause delay
    parallel:
        linear 1.2 alpha 0.8
        linear 2.8 alpha 0.0
    parallel:
        ease 4.0 ypos (y - 80)
    repeat
