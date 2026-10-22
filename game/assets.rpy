# Landscapes share a virtual canvas regardless of source size/aspect ratio.
init python:
    def landscape(filename):
        return Transform(filename, xysize=(1920, 1080), fit="cover", align=(0.5, 0.5))

image bg steppe = landscape("ural_art/steppe.jpg")
image bg cave = landscape("ural_art/cave.jpg")
image bg mountains = landscape("ural_art/mountains.jpeg")
image bg forest = landscape("ural_art/forest.jpg")
image bg settlement = landscape("ural_art/settlement.jpg")
image bg storm = landscape("ural_art/storm.jpg")
image bg sky = landscape("ural_art/sky.jpg")
image bg underworld = landscape("ural_art/underworld.jpg")
image bg spring = landscape("ural_art/spring.jpg")
image bg battle = landscape("ural_art/battle.jpg")
image bg dawn = landscape("ural_art/dawn.jpg")
image menu landscape = landscape("ural_art/mountains.jpeg")

# Existing character artwork is retained.
image ural = "images/ural.png"
image shulgen = "images/shulgen.png"
image humay = "images/humay.png"
image yanbide = 'image/'

transform center_character:
    xysize (650, 880)
    fit "contain"
    align (0.5, 1.0)
transform left_character:
    xysize (600, 860)
    fit "contain"
    align (0.20, 1.0)
transform right_character:
    xysize (600, 860)
    fit "contain"
    align (0.80, 1.0)

transform landscape_drift:
    align (0.5, 0.5)
    zoom 1.04
    ease 14.0 xoffset 18
    ease 14.0 xoffset -18
    repeat
