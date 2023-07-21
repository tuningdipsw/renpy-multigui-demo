define s = Character('STEPHANIE')
define l = Character('LUCILLIUS')
define s_nvl = Character('', kind=nvl)
# define narrator = nvl_narrator
define polarity = "default"

image s neutral = "s_neutral.png"
image s curious = "s_curious.png"
image l neutral = "l_neutral.png"
image l curious = "l_curious.png"
image bg snow = im.Scale("lunabg_placeholder.png", game_width, game_height)
image bg field = im.Scale("solbg_placeholder.png", game_width, game_height)
image bg default = im.Scale("main_menu.png", game_width, game_height)

label start:
    scene bg default
    "test default polarity"

    # issue: quick menu buttons look bad during NVL because of polarity,
    # so we end up manually setting default polarity before NVL sections
    $ polarity = "default"

    s_nvl "Narukami-kun! Help! The multiverse is in danger! Ruby Rose from RWBY™️ and"
    s_nvl "Ragna=the=Bloodedge from Blazblue™️  Central Fiction™️ are currently looking to assemble an"
    s_nvl "elite group of multidimensional heroes in order to stop the ICONIC Marvel™️ villain, Thanos,"
    s_nvl "from wiping out half the known multiverse. And we're gonna need someone with a 17f comboable"
    s_nvl "safe on block overhead to do it."
    nvl clear

    $ polarity = "sun"

    show s neutral at right
    s '"Hi there! How was class?"'

    # menu menu_test_sun:
    #     "Choices"
    #     "choice 1":
    #         "1"
    #     "choice 2":
    #         "2"

    $ polarity = "moon"
    show l neutral at left
    l '"Good..."'

    "I can't bring myself to admit that it all went in one ear and out the other."

    # menu menu_test_moon:
    #     "Choices"
    #     "choice 1":
    #         "1"
    #     "choice 2":
    #         "2"

    $ polarity = "sun"
    scene bg snow
    show s curious at right
    s '"Are you going home now? Wanna walk back with me?"'

    $ polarity = "moon"
    show l curious at left
    l '"Sure!"'
