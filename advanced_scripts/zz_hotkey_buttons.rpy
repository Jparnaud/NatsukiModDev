


init python:


    def HKBHideButtons():



        config.overlay_screens.remove("hkb_overlay")
        renpy.hide_screen("hkb_overlay")


    def HKBShowButtons():



        config.overlay_screens.append("hkb_overlay")

init -1 python in hkb_button:



    enabled = True







define gui.hkb_button_width = 120
define gui.hkb_button_height = None
define gui.hkb_button_tile = False
define gui.hkb_button_borders = Borders(100, 5, 100, 5)
define gui.hkb_button_text_font = gui.default_font
define gui.hkb_button_text_size = gui.text_size
define gui.hkb_button_text_xalign = 0.5
define gui.hkb_button_text_idle_color = "#000"
define gui.hkb_button_text_hover_color = "#fa9"

define gui.hkb_button_black_width = 120
define gui.hkb_button_black_height = None
define gui.hkb_button_black_tile = False
define gui.hkb_button_black_borders = Borders(100, 5, 100, 5)
define gui.hkb_button_black_text_font = gui.default_font
define gui.hkb_button_black_text_size = gui.text_size
define gui.hkb_button_black_text_xalign = 0.5
define gui.hkb_button_black_text_idle_color = "#000"
define gui.hkb_button_black_text_hover_color = "#fa9"

define gui.talk_button_width = 120
define gui.talk_button_height = None
define gui.talk_button_tile = False
define gui.talk_button_borders = Borders(100, 5, 100, 5)
define gui.talk_button_text_font = gui.default_font
define gui.talk_button_text_size = gui.text_size
define gui.talk_button_text_xalign = 0.5
define gui.talk_button_text_idle_color = "#000"
define gui.talk_button_text_hover_color = "#fa9"
default allow_boop = None



style hkb_vbox is vbox
style hkb_button is button
style hkb_button_text is button_text

style hkb_vbox_black is vbox
style hkb_button_black is button
style hkb_button_black_text is button_text

style talk_vbox is vbox
style talk_button is button
style talk_button_text is button_text

style hkb_vbox:
    spacing 0

style hkb_vbox_black:
    spacing 0

style hkb_button is default:
    properties gui.button_properties("hkb_button")
    idle_background "mod_assets/buttons/hkb_idle_background.png"
    hover_background "mod_assets/buttons/hkb_hover_background.png"

    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style hkb_button_black is default:
    properties gui.button_properties("hkb_button_black")
    idle_background "mod_assets/buttons/hkb_idle_background_black.png"
    hover_background "mod_assets/buttons/hkb_hover_background_black.png"

    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style hkb_button_text is default:
    properties gui.button_text_properties("hkb_button")
    outlines []

style hkb_button_text_black is default:
    properties gui.button_text_properties("hkb_button_black")
    outlines []

style talk_vbox:
    spacing 0

style talk_button is default:
    properties gui.button_properties("talk_button")
    idle_background "mod_assets/buttons/talk_idle_background.png"
    hover_background "mod_assets/buttons/talk_hover_background.png"

    hover_sound gui.hover_sound
    activate_sound gui.activate_sound


style talk_button_text is default:
    properties gui.button_text_properties("talk_button")
    outlines []

style hkbd_vbox is vbox
style hkbd_button is button
style hkbd_button_text is button_text

style hkbd_vbox:
    spacing 0

style hkbd_button is default:
    properties gui.button_properties("hkb_button")
    idle_background "mod_assets/buttons/hkb_disabled_background.png"
    hover_background "mod_assets/buttons/hkb_disabled_background.png"

style hkbd_button_text is default:

    font gui.default_font
    size gui.text_size
    xalign 0.5
    idle_color "#000"
    hover_color "#000"
    outlines []

style hkbd_button_black is default:
    properties gui.button_properties("hkb_button_black")
    idle_background "mod_assets/buttons/hkb_disabled_background_black.png"
    hover_background "mod_assets/buttons/hkb_disabled_background_black.png"

style hkbd_button_text_black is default:

    font gui.default_font
    size gui.text_size
    xalign 0.5
    idle_color "#000"
    hover_color "#000"
    outlines []

style talkd_vbox is vbox
style talkd_button is button
style talkd_button_text is button_text

style talkd_vbox_black is vbox
style talkd_button_black is button
style talkd_button_text_black is button_text

style talkd_vbox:
    spacing 0

style talkd_button is default:
    properties gui.button_properties("hkb_button")
    idle_background "mod_assets/buttons/hkb_disabled_background.png"
    hover_background "mod_assets/buttons/hkb_disabled_background.png"

style talkd_button_text is default:

    font gui.default_font
    size gui.text_size
    xalign 0.5
    idle_color "#000"
    hover_color "#000"
    outlines []


screen hkb_overlay:

    zorder 50

    style_prefix "hkb"

    vbox:
        xalign 0.05
        yalign 0.95

        if persistent.blackout:
            if allow_dialogue:
                textbutton _("Talk"):
                    action Jump("talkmenu")
                    style "hkb_button_black"
            else:
                textbutton _("Talk"):
                    action NullAction()
                    style "hkbd_button_black"
        else:
            if allow_dialogue:
                textbutton _("Talk") action Jump("talkmenu")
            else:
                textbutton _("Talk"):
                    action NullAction()
                    style "hkbd_button"
        if persistent.date == "":
            if allow_dialogue:
                textbutton _("Extras") action Jump("extrasmenu")
            else:
                textbutton _("Extras"):
                    action NullAction()
                    style "hkbd_button"

        if persistent.natsuki_love:
            if persistent.natsuki_emotion == "Happy" or persistent.natsuki_emotion == "Casual":
                if allow_dialogue:
                    textbutton _("Dates") action Jump("datemenu")
                else:
                    textbutton _("Dates"):
                        action NullAction()
                        style "hkbd_button"
        elif persistent.natsuki_emotion == "Happy" or persistent.natsuki_emotion == "Casual":
            if allow_dialogue:
                textbutton _("Places") action Jump("datemenu")
            else:
                textbutton _("Places"):
                    action NullAction()
                    style "hkbd_button"
        if persistent.date == "":
            if allow_dialogue:
                textbutton _("Music") action Jump("musicmenu")
            else:
                textbutton _("Music"):
                    action NullAction()
                    style "hkbd_button"
        else:
            if allow_dialogue:
                textbutton _("Action") action Jump("actions")
            else:
                textbutton _("Action"):
                    action NullAction()
                    style "hkbd_button"

    text "v[config.version]":
                xalign 1.0 yalign 1.0
                xoffset -10 yoffset -10
                style "main_menu_version"

    vbox:
        imagebutton:
            xpos 546 ypos 273
            idle "mod_assets/buttons/boopindicator.png"
            hover "mod_assets/buttons/boopindicator.png"
            action [If(allow_dialogue, true=Jump("ch30_boop"))]

screen fight:

    zorder 50

    style_prefix "hkb"


    vbox:
        xalign 0.05
        yalign 0.95


        textbutton _("Fight") action Jump("fight")

        textbutton _("Act") action Jump("act")

        textbutton _("Codes") action Jump("codes")

        textbutton _("Mercy") action Jump("mercy")

    xpos 424 ypos 814
    label _("HP: [hp]")

screen talking_new:

    zorder 50

    style_prefix "talk"


    vbox:
        xalign 500
        yalign 100

        vbox:
            textbutton _("1") action Jump("normaltalkmenu")
            xpos 867 ypos 137

            textbutton _("2") action Jump("normaltalkmenu2")

            textbutton _("3") action Jump("normaltalkmenu3")

            textbutton _("4") action Jump("normaltalkmenu4")

            textbutton _("5") action Jump("normaltalkmenu5")

            textbutton _("6") action Jump("normaltalkmenu6")

            textbutton _("7") action Jump("normaltalkmenu7")

            textbutton _("8") action Jump("normaltalkmenu8")

screen talking_new2:

    zorder 50

    style_prefix "talk"


    vbox:
        xalign 500
        yalign 100

        vbox:
            textbutton _("X") action Hide("talking2"), Show("talking")
            xpos 867 ypos 137

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
