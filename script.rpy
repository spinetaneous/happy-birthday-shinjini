# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define shinjini = Character(_("Shinjini"), color = "#47e0ff", image = "shinjini")
    image shinjini= "shinjini_normal.png"
    image shinjini blush = "shinjini_blush.png"
    image shinjini glasses = "shinjini_glasses.png"
    image side shinjini = "shinjini_portrait.png"
define irene = Character(_("Irene"), color = "#0000ff", image = "irene")
    image irene = "irene_normal.png"
    image side irene = "irene_portrait.png"
define steven = Character(_("Irene"), color = "#00ff00", image = "steven")
    image steven = "steven_normal.png"
    image side steven = "steven_portrait.png"
define aristotle = Character(_("Aristotle"), color = "#DEB887", image = "aristotle")
    image aristotle = "aristotle_normal.png"
	image side

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
