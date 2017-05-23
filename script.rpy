# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define shinjini = Character(_("Shinjini"), color = "#47e0ff", image = "shinjini")
image shinjini = "c_shinjini_normal.png"
image shinjini blush = "c_shinjini_blush.png"
image shinjini glasses = "c_shinjini_glasses.png"
image side shinjini = "shinjini_portrait.png"

define irene = Character(_("Irene"), color = "#0000ff", image = "irene")
image irene = "irene_normal.png"
image side irene = "irene_portrait.png"

define steven = Character(_("Masked Man"), color = "#00ff00", image = "steven")
image steven = "steven_normal.png"
image side steven = "steven_portrait.png"

define aristotle = Character(_("Aristotle"), color = "#DEB887", image = "aristotle")
image aristotle  = "aristotle_normal.png"
image side aristotle = "aristotle_portrait.png"

define nicola = Character(_("Noircola"), color = "#00E5EE", image = "nicola")
image nicola = "c_noire_normal.png"
image side nicola = "noire_portrait.png"

define james = Character(_("Juni"), color = "#00E5EE", image = "james")
image james = "c_uni_normal.png"
image side james = "uni_portrait.png"

image bg bedroom = "bg/bg_bedroom.jpg"
image bg hall4 = "bg/bg_hall4.jpg"
image bg lounge4 = "bg/bg_lounge4.jpg"
image bg stairs = "bg/bg_stairs.jpg"
image bg lounge3 = "bg/bg_lounge3.jpg"

define mus_opening = "music/m_magicant.mp3"
define mus_relax = "music/pisaloon.mp3"
define mus_nowwhat = "music/uranus.mp3"
define mus_alone = "music/m_sspace.mp3"
define mus_scary = "music/m_darkness.mp3"
define mus_steven = "music/m_mask.mp3"
define mus_nicola = "music/m_race.mp3"


transform walkin(initialx, endx):
    zoom 0.8
    xalign initialx yalign 1.0
    linear 1.5 xalign endx
    pause (.5)

transform appear (x):
    zoom .8
    xalign x yalign 1.0
    pause (.5)
# The game starts here.

label start:


    scene bg bedroom with fade
    play music mus_opening


    # These display lines of dialogue.

    "Mmmm... Bunnies... I wanna be a bunny..."
    "Mmmm... Bob, I love you too..."
    "Shinjini, wake up!"
    "Huh?"
    
    show irene at appear(.75) with dissolve
    irene "Shinjini, get the @#$* up!"
    show shinjini at walkin(-.9, .2)
    shinjini "Nauoooo..."
    irene "lol"
    show steven at appear(.5) with dissolve
    steven "I SHALL CONSUME HUMANITY."
    hide steven with dissolve
    show nicola at appear(.5) with dissolve
    nicola "Oh, why am I a girl?!"
    hide irene
    show james at appear(.8) with dissolve
    james "Feels bad, man."


    shinjini "You've created a new Ren'Py game."

    shinjini "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
