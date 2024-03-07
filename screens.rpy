screen lovelustchanger():
    tag menu
    add define_mods_images["mod_menu"]
    use menu_mod(_("Меню изменения очков"), scroll="viewport"):
        style_prefix "aff"
        vpgrid:
            cols 5
            align (1, 1)
            spacing 80
            imagebutton:
                idle "mods/lovelustchanger/idle_button_all.png"
                hover "mods/lovelustchanger/hover_button_all.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='all')]
            imagebutton:
                idle "chikathumb1.png"
                hover "chikathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='chika')]
            imagebutton:
                idle "yumithumb1.png"
                hover "yumithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='yumi')]
            imagebutton:
                idle "ayanethumb1.png"
                hover "ayanethumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='ayane')]
            imagebutton:
                idle "sanathumb1.png"
                hover "sanathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='sana')]
            imagebutton:
                idle "makotothumb1.png"
                hover "makotothumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='makoto')]
            imagebutton:
                idle "mikuthumb1.png"
                hover "mikuthumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='miku')]
            imagebutton:
                idle "futabathumb1.png"
                hover "futabathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='futaba')]
            imagebutton:
                idle "rinthumb1.png"
                hover "rinthumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='rin')]
            imagebutton:
                idle "amithumb1.png"
                hover "amithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='ami')]
            imagebutton:
                idle "mayathumb1.png"
                hover "mayathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='maya')]
            imagebutton:
                idle "mollythumb1.png"
                hover "mollythumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='molly')]
            imagebutton:
                idle "tsuneyothumb1.png"
                hover "tsuneyothumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='tsuneyo')]
            imagebutton:
                idle "utathumb1.png"
                hover "utathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='uta')]
            imagebutton:
                idle "iothumb1.png"
                hover "iothumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='io')]
            imagebutton:
                idle "nodokathumb1.png"
                hover "nodokathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='nodoka')]
            imagebutton:
                idle "otohathumb1.png"
                hover "otohathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='otoha')]
            imagebutton:
                idle "toukathumb1.png"
                hover "toukathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='touka')]
            imagebutton:
                idle "yasuthumb1.png"
                hover "yasuthumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='yasu')]
            imagebutton:
                idle "norikothumb1.png"
                hover "norikothumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='noriko')]
            imagebutton:
                idle "kirinthumb1.png"
                hover "kirinthumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='kirin')]
            imagebutton:
                idle "sarathumb1.png"
                hover "sarathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='sara')]
            imagebutton:
                idle "harukathumb1.png"
                hover "harukathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='haruka')]
            imagebutton:
                idle "kaorithumb1.png"
                hover "kaorithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='kaori')]
            imagebutton:
                idle "chinamithumb1.png"
                hover "chinamithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='chinami')]
            imagebutton:
                idle "karinthumb1.png"
                hover "karinthumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='karin')]
            imagebutton:
                idle "makithumb1.png"
                hover "makithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='maki')]
            imagebutton:
                idle "yukithumb1.png"
                hover "yukithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='yuki')]
            imagebutton:
                idle "nikithumb1.png"
                hover "nikithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='niki')]
            imagebutton:
                idle "wakanathumb1.png"
                hover "wakanathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='wakana')]
            imagebutton:
                idle "osakothumb1.png"
                hover "osakothumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='osako')]
            imagebutton:
                idle "tsubasathumb1.png"
                hover "tsubasathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='tsubasa')]
            imagebutton:
                idle "tsukasathumb1.png"
                hover "tsukasathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='tsukasa')]
            imagebutton:
                idle "imanithumb1.png"
                hover "imanithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='imani')]
            imagebutton:
                idle "rikathumb1.png"
                hover "rikathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='rika')]
            imagebutton:
                idle "naothumb1.png"
                hover "naothumb2.png"
                xalign 0.2 yalign 0.5
                focus_mask True
                action [ShowMenu('lovelustchange', selected_girl='nao')]
            null
            null
            null
            null

screen lovelustchange(selected_girl):
    tag menu
    add define_mods_images["mod_menu"]
    use menu_mod(_("Меню изменения очков")):
        style_prefix "aff"
        if selected_girl == 'all':
            grid 1 2:
                ypos 70
                imagebutton:
                    idle define_mods_images["idle_lovelust_button_1"]
                    hover define_mods_images["hover_lovelust_button_1"]
                    action Show('value_input', message='Введите новое значение любви', ok_action=Function(FinishEnterLoveLust, selected_girl, 'love'), alloww='1234567890')
                imagebutton:
                    idle define_mods_images["idle_lovelust_button_2"]
                    hover define_mods_images["hover_lovelust_button_2"]
                    action Show('value_input', message='Введите новое значение вожделения', ok_action=Function(FinishEnterLoveLust, selected_girl, 'lust'), alloww='1234567890')
        else:
            grid 1 2:
                text "Любовь: {}".format(globals()[selected_girl + '_love'])
                if selected_girl + '_lust' in globals():
                    text "Вожделение: {}".format(globals()[selected_girl + '_lust'])
                else:
                    text "Вожделение: N/A"
            grid 1 2:
                ypos 70
                imagebutton:
                    idle define_mods_images["idle_lovelust_button_1"]
                    hover define_mods_images["hover_lovelust_button_1"]
                    action Show('value_input', message='Введите новое значение любви', ok_action=Function(FinishEnterLoveLust, selected_girl, 'love'), alloww='1234567890')
                if selected_girl + '_lust' in globals() and not globals()[selected_girl + '_lust'] == 'N/A':
                    imagebutton:
                        idle define_mods_images["idle_lovelust_button_2"]
                        hover define_mods_images["hover_lovelust_button_2"]
                        action Show('value_input', message='Введите новое значение вожделения', ok_action=Function(FinishEnterLoveLust, selected_girl, 'lust'), alloww='1234567890')
                else:
                    null