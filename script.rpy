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
image irene flip = im.Flip("irene_normal.png", horizontal=True)
image side irene = "irene_portrait.png"

define steven = Character(_("Masked Man"), color = "#00ff00", image = "steven")
image steven = "steven_normal.png"
image side steven = "steven_portrait.png"

define aristotle = Character(_("Aristotle"), color = "#DEB887", image = "aristotle")
image aristotle  = "c_aristotle_normal.png"
image side aristotle = "aristotle_portrait.png"

define nicola = Character(_("Noircola"), color = "#00E5EE", image = "nicola")
image nicola = "c_noire_normal.png"
image side nicola = "noire_portrait.png"

define james = Character(_("Juni"), color = "#00E5EE", image = "james")
image james = "c_uni_normal.png"
image side james = "uni_portrait.png"

define austin = Character(_("4u571n"), color = "#8b0000", image = "austin")
image austin:
    "c_giygaustin/011.png"
    pause .5
    "c_giygaustin/012.png"
    pause .5
    "c_giygaustin/013.png"
    pause .5
    "c_giygaustin/014.png"
    pause .5
    "c_giygaustin/013.png"
    pause .5
    "c_giygaustin/012.png"
    pause .5
    repeat
image side austin_portrait = "austin_portrait.png"

image investigation movie = Movie(channel="movie", play="bg/investigation.mkv")
image irene_phone = "bg/c_irenephone.png"

image m_0 = "mess/m_0.jpg"
image m_1 = "mess/m_1.jpg"
image m_2 = "mess/m_2.jpg"
image m_3 = "mess/m_3.jpg"
image m_4 = "mess/m_4.jpg"

image m_5a = "mess/m_5a.jpg"
image m_6a = "mess/m_6a.jpg"
image m_7a = "mess/m_7a.jpg"
image m_8a = "mess/m_8a.jpg"
image m_9a = "mess/m_9a.jpg"
image m_10a = "mess/m_10a.jpg"
image m_11a = "mess/m_11a.jpg"

image m_5b = "mess/m_5b.jpg"
image m_6b = "mess/m_6b.jpg"
image m_7b = "mess/m_7b.jpg"
image m_8b = "mess/m_8b.jpg"
image m_9b = "mess/m_9b.jpg"
image m_10b = "mess/m_10b.jpg"

image m_5c = "mess/m_5c.jpg"
image m_6c = "mess/m_6c.jpg"
image m_7c = "mess/m_7c.jpg"
image m_8c = "mess/m_8c.jpg"
image m_9c = "mess/m_9c.jpg"
image m_10c = "mess/m_10c.jpg"
image m_11c = "mess/m_11c.jpg"

image bg black = "bg/bg_black.jpg"
image bg white = "bg/bg_white.jpg"
image bg bedroom = "bg/bg_bedroom.jpg"
image bg bedroom_r = "bg/bg_bedroom_r.jpg"
image bg hall4 = "bg/bg_hall4.jpg"
image bg lounge4 = "bg/bg_lounge4.jpg"
image bg stairs = "bg/bg_stairs.jpg"
image bg lounge3 = "bg/bg_lounge3.jpg"
image bg lounge3_garbage = "bg/bg_lounge3_garbage.jpg"
image bg lounge3_r:
        "bg/data/000.png"
        pause .1
        "bg/data/001.png"
        pause .1
        "bg/data/002.png"
        pause .1
        "bg/data/003.png"
        pause .1
        "bg/data/004.png"
        pause .1
        "bg/data/005.png"
        pause .1
        "bg/data/006.png"
        pause .1
        "bg/data/007.png"
        pause .1
        "bg/data/008.png"
        pause .1
        "bg/data/009.png"
        pause .1
        "bg/data/010.png"
        pause .1
        "bg/data/011.png"
        pause .1
        "bg/data/010.png"
        pause .1
        "bg/data/009.png"
        pause .1
        "bg/data/008.png"
        pause .1
        "bg/data/007.png"
        pause .1
        "bg/data/006.png"
        pause .1
        "bg/data/005.png"
        pause .1
        "bg/data/004.png"
        pause .1
        "bg/data/003.png"
        pause .1
        "bg/data/002.png"
        pause .1
        "bg/data/001.png"
        pause .1
        repeat


define mus_opening = "music/m_magicant.mp3"
define mus_relax = "music/pisaloon.mp3"
define mus_nowwhat = "music/uranus.mp3"
define mus_spooky = "music/m_sspace.mp3"
define mus_alone = "music/j_ship.mp3"
define mus_scary = "music/m_darkness.mp3"
define mus_steven = "music/m_mask.mp3"
define mus_nicola = "music/m_race.mp3"
define mus_giygas = "music/giygas.mp3"

define scream = "sound/Wilhelm_Scream.ogg"
define scare_chord = "sound/scare_chord.mp3"
define caught_pokemon = "sound/caught_pokemon.mp3"
define message = "sound/message.mp3"
define message_sent = "sound/message_sent.mp3"
define clang = "sound/clang.mp3"

transform walkin(initialx, endx):
    zoom 0.8
    xalign initialx yalign 1.0
    linear 1.5 xalign endx
    pause (.5)

transform appear (x):
    zoom .8
    xalign x yalign 1.0
    pause (.5)


transform imgpos:
    zoom .973
    xalign 0.5 
    yanchor 0
    ypos 58
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
    show irene flip at walkin (-.9, .1)
    show shinjini at walkin (-.9, .25)
    shinjini "Oh, look, There's Austin. He doesn't look very happy right now."
    irene "Wut.{p=1} The.{p=1} #$@*."
    scene bg lounge3_r with dissolve
    play music mus_giygas fadein 1
    pause 3
    show austin at appear(.5) with dissolve
    pause 1
    austin "Oh, hey Shinjini, Irene."
    james "Ah!!! So disturbing. I think I died on the inside a bit."
    irene "Why do you look like a swirly energy thingie, lol?"
    austin "I don't know, but I need to study chem."
    irene "Don't you have more important things? Like, how can you even study?"
    austin "I can still hold a pencil."
    austin "GPA is forever."
    shinjini "Shinjini wonders if you are possessed by a demon. Is he a nice demon?"
    austin "Uhhh... Probably not. But I have a midterm to study for now, so go away."
    shinjini "Awww..."
    irene "But we live here, fool. You came here."
    austin "Go away."
    
    stop music
    
    scene bg lounge3_garbage with fade
    play music mus_alone
    show james at walkin (-.9, .35)
    show irene flip at walkin (-.9, .1)
    show nicola at walkin (1.9, .9)
    show shinjini at walkin (1.9, .65)

    
    nicola "Austin wasn't as helpful as I thought he'd be. We need to look for some leads."
    irene "Almost like we didn't know how to incorporate him into the plot."
    nicola "Anyway, we need to focus on finding out why people are turning into-{p=.75}{nw}"
    stop music
    "???" "BOO!"
    with hpunch
    play sound scream
    with hpunch
    james "AAAAAAAHHHHH!"
    play music mus_alone fadein 1
    shinjini "Sounds like Steven. Is Steven around?"
    irene "Steven, where are you?!!?!"
    play sound message
    pause .75
    irene "Message..."
    
    scene investigation movie with fade
    pause 2
    show irene_phone with dissolve:
        xalign 0.5
    irene "Let's see..."
    show m_0 at imgpos with dissolve
    pause 1.5
    irene "Steven contacted me."
    shinjini "Ask him where Steven is."
    play sound message_sent
    show m_1 at imgpos
    hide m_0
    irene "Hmm..."
    pause .5
    play sound message_sent
    show m_2 at imgpos
    hide m_1
    pause 2
    play sound message_sent
    show m_3 at imgpos
    hide m_2
    pause 2
    play sound message_sent
    show m_4 at imgpos
    hide m_3
    pause 2
    
    irene "Ugh, Steven..."
    irene "How should I respond..."
    menu:
           "Inquire regarding his introductory statement requesting assistance.":
            jump help
           "Awe him with the power of expletives and profanity.":
            jump cuss
           "Engage in a rather thoughtful dialectic while musing about the existences of objects.":
            jump wut
           
label help:
    play sound message_sent
    show m_5a at imgpos
    hide m_4
    pause 2
    play sound message_sent
    show m_6a at imgpos
    hide m_5a
    pause 2
    play sound message_sent
    show m_7a at imgpos
    hide m_6a
    pause 2
    play sound message_sent
    show m_8a at imgpos
    hide m_7a
    pause 2
    play sound message_sent
    show m_9a at imgpos
    hide m_8a
    pause 2
    play sound message_sent
    show m_10a at imgpos
    hide m_9a
    pause 2
    play sound message_sent
    show m_11a at imgpos
    hide m_10a
    pause 2
    
    hide m_11a with dissolve
    jump cont
    
label cuss:
    play sound message_sent
    show m_5b at imgpos
    hide m_4
    pause 2
    play sound message_sent
    show m_6b at imgpos
    hide m_5b
    pause 2
    play sound message_sent
    show m_7b at imgpos
    hide m_6b
    pause 2
    play sound message_sent
    show m_8b at imgpos
    hide m_7b
    pause 2
    play sound message_sent
    show m_9b at imgpos
    hide m_8b
    pause 2
    play sound message_sent
    show m_10b at imgpos
    hide m_9b
    pause 2
    
    hide m_10b with dissolve
    jump cont
    
label wut:
    play sound message_sent
    show m_5c at imgpos
    hide m_4
    pause 2
    play sound message_sent
    show m_6c at imgpos
    hide m_5c
    pause 2
    play sound message_sent
    show m_7c at imgpos
    hide m_6c
    pause 2
    play sound message_sent
    show m_8c at imgpos
    hide m_7c
    pause 2
    play sound message_sent
    show m_9c at imgpos
    hide m_8c
    pause 2
    play sound message_sent
    show m_10c at imgpos
    hide m_9c
    pause 1
    irene "Steven..!"
    shinjini "Just make him come over here, then."
    pause 1
    play sound message_sent
    show m_11c at imgpos
    hide m_10c
    pause 2
    play sound message_sent
    show m_12c at imgpos
    hide m_11c
    pause 2
    play sound message_sent
    show m_13c at imgpos
    hide m_12c
    pause 2
    play sound message_sent
    show m_14c at imgpos
    hide m_13c
    pause 2
    
    hide m_14c with dissolve
    jump cont
    
label cont:
    irene "Steven should appear soo-{p=.5}{nw}"
    stop music
    play sound clang
    with hpunch
    irene "Huh?"
    shinjini "The recycling bin! Is it also possessed by a demon?"
    
    scene bg lounge3_garbage with fade
    show james at appear ( .15)
    show irene flip at appear (.01)
    show nicola at appear (.99)
    show shinjini at appear (.85)
    
    play sound clang
    with hpunch
    nicola "I've got a bad feeling about this..."
    james "Doesn't seem to be very friendly..."
    
    #show explosion at appear(.5)
    #
    
    # This ends the game.

    return
