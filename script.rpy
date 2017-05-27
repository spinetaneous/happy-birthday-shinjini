# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define shinjini = Character(_("Shinjini"), color = "#47e0ff", image = "shinjini")
image shinjini = "c_shinjini_normal.png"
image shinjini blush = "c_shinjini_blush.png"
image shinjini glasses = "c_shinjini_glasses.png"
image side shinjini = "shinjini_portrait.png"

define irene = Character(_("Irene"), color = "#0000ff", image = "irene")
image irene = "irene_normal.png"
<<<<<<< HEAD
image irene flip = im.Flip("irene_normal.png", horizontal=True)
=======
>>>>>>> dcf0f874a33272aa112dfb1c87bba5915bce99a2
image side irene = "irene_portrait.png"

define steven = Character(_("Masked Man"), color = "#00ff00", image = "steven")
image steven = "steven_normal.png"
image side steven = "steven_portrait.png"

define aristotle = Character(_("Aristotle"), color = "#DEB887", image = "aristotle")
<<<<<<< HEAD
image aristotle  = "c_aristotle_normal.png"
image side aristotle = "aristotle_portrait.png"

define nicola = Character(_("Noircola"), color = "#00E5EE", image = "nicola")
image nicola = "c_noire_normal.png"
image side nicola = "noire_portrait.png"
=======
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
>>>>>>> dcf0f874a33272aa112dfb1c87bba5915bce99a2

define james = Character(_("Juni"), color = "#00E5EE", image = "james")
image james = "c_uni_normal.png"
image side james = "uni_portrait.png"

<<<<<<< HEAD
define austin = Character(_("4u571n"), color = "#8b0000", image = "austin")
image austin_animated:
    "c_giygaustin/011.png"
    pause .2
    "c_giygaustin/012.png"
    pause .2
    "c_giygaustin/013.png"
    pause .2
    "c_giygaustin/014.png"
    pause .2
    "c_giygaustin/013.png"
    pause .2
    "c_giygaustin/012.png"
    pause .2
    repeat
image side austin_portrait = "austin_portrait.png"

image bg bedroom = "bg/bg_bedroom.jpg"
image bg bedroom_r = "bg/bg_bedroom_r.jpg"
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

define scream = "sound/Wilhelm_Scream.ogg"
define scare_chord = "sound/scare_chord.mp3"
define caught_pokemon = "sound/caught_pokemon.mp3"
=======

    scene bg bedroom with fade
    play music mus_opening

>>>>>>> dcf0f874a33272aa112dfb1c87bba5915bce99a2

transform walkin(initialx, endx):
    zoom 0.8
    xalign initialx yalign 1.0
    linear 1.5 xalign endx
    pause (.5)

<<<<<<< HEAD
transform appear (x):
    zoom .8
    xalign x yalign 1.0
    pause (.5)
# The game starts here.

label start:


    scene bg bedroom with fade


    # These display lines of dialogue.

    "Mmmm... Math... Should I get up..."
    "..."
    "...Nah, too sleepy..."
    "..."
    scene bg bedroom with fade
    play music mus_opening
    show irene at appear(.75) with dissolve
    irene "Shinjini, wake up."
    show shinjini at walkin(-.9, .2)
    shinjini "Nauoooo..."
    shinjini "Wait, why is your hair black?"
    irene "? My natural hair color is black?"
    shinjini "Wait, why is your hair now blond?"
    irene "...? Maybe you need to put your glasses on."
    show shinjini glasses
    shinjini "But I'm already wearing glasses..."
    show shinjini
    irene "Anyway, it's already 1 in the afternoon, so let's go get lunch."
    stop music
    play sound scream
    with hpunch
=======
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
>>>>>>> dcf0f874a33272aa112dfb1c87bba5915bce99a2

    irene "Ooh, spooky. :o"
    shinjini "Was that... James?!"
    irene "Probably? Let's go check up on him."
    shinjini "He's probably okay..."
    shinjini "{cps=*.2}...?{/cps}!?!? What the...{nw}"
    scene bg bedroom_r
    hide shinjini
    hide irene
    play music mus_scary
    play sound scare_chord
    show aristotle:
        xalign 0.5
        yalign 0.1
    with hpunch
    aristotle "Die."
    shinjini "Oh, my baby! He's talking!"
    irene "Dude, remember that one time we talked about this happening?"
    irene "Now I can say it! Ahem..."
    irene "I am okay with this."
    shinjini "That was a hypothetical situation though... I didn't think it would actually happen."
    irene "But why did your baby tell us to die?"
    shinjini "Maybe he just wants a hug."
    aristotle "Your souls are mine."
    shinjini "That's fine, we don't have any."
    irene "LOLOL you're getting a pretty sh@#$y deal here, buddy."
    aristotle "Your friends already have fallen to me."
    shinjini "But my friends are in India..."
    irene "And my 707 cushion is right next to me..."
    aristotle "Haruka Nanase is mine."
    shinjini "Oh, @#$^&!"
    irene "Oh no, your lover!"
    shinjini "Back off, Aristotle, he's mine!"
    aristotle "Haruka Nanase is not needed anymore in this world..."
    hide aristotle with dissolve
    stop music fadeout 2
    scene bg bedroom with fade
    shinjini "Naauuoooooo! He flew out the door!"
    irene "We have to save your husband!"
    
    scene bg hall4 with fade
    show irene flip at walkin(-.9, .1)
    show shinjini at walkin (-.9, .25)
    shinjini "Aw, Aristotle flew off... We need to get Haruka back!"
    irene "Oh yeah, what happened to James?"
    "???" "A fate worse than death has occurred to him. And myself."
    shinjini "Huh? Oh, Nicola, I was wondering{cps=*.1}...{/cps} What the @#$?!"
    show nicola at walkin (1.9, .75)
    shinjini "You got turned into a waifu!?"
    play music mus_nicola
    nicola "Yep. Worst morning ever. I wake up and realize I have a skirt and twintails."
    irene "LMAO are you wearing a bra, too?"
    nicola "{cps=*.1}... ... {/cps}"
    nicola "Anyway, I can't find anyone-{p=.5}{nw}"
    irene "OMG ARE YOU WEARING PANTIES TOO?????"
    nicola "........................"
    nicola "{b} ANYWAY... {/b}"
    nicola "I can't find anyone. The building is almost entirely abandoned.
            Your guess is as good as mine. Even Bob and my roommates disappeared..."
    nicola "Also, on my trip up to the fourth floor, I found this guy."
    "???" "Ooooooooh, so tilted..."
    show james at walkin (1.9, .65)
    show nicola at walkin (.75, .9)
    james "I'm also a girl. FeelsBadMan..."
    nicola "Well, that doesn't seem to change anything from before."
    james "Oooh, the burns! They never stop even in a VN, do they?"
    shinjini "Well, now both of you are real pretty boys! Why are you waifus?"
    nicola "No idea. Irene's drawings remain on my wall, though. I look exactly
            like Noire from that {i}Neptunia{/i} series. James here looks like
            Uni from the same series. I wonder if others got waifu'd?"
    irene "Be cool if we ran into my waifu self."
    shinjini "Oh, two Irenes! That'd be fun!"
    nicola "Anyway, we'll probably join your party."
    shinjini "Huh? What do you mean?"
    stop music
    play sound caught_pokemon
    hide nicola with dissolve
    "NOIRE NICOLA HAS JOINED THE PARTY!"
    james "Wha?!?! How did he do that?!"
    nicola "Very carefully."
    james "I'll try it too. Woo!"
    play sound caught_pokemon
    hide james with dissolve
    "UNI JAMES HAS JOINED THE PARTY!"
    james "gg ez"
    irene "Anyway, better look for others. Himashi and Demini aren't in their room."
    shinjini "Aw, let's go down to the third floor..."
    
    scene bg lounge3 with fade
    
    
    # This ends the game.

    return
