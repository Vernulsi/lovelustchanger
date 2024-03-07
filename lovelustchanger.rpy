init python:
    def FinishEnterLoveLust(selected_girl, prefix):
        global value
        if value == '':
            return
        if selected_girl == 'all':
            for i in [i[0] for i in globals().items() if i[0].endswith('_'+prefix)]: globals()[i] = int(value)
        else:
            globals()[selected_girl + '_' + prefix] = int(value)
        renpy.hide_screen("value_input")
        value = ''
        renpy.show_screen('dialog', message="Промотай для сохранения результата!", ok_action=Function(renpy.hide_screen, 'dialog'))