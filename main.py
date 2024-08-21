import PySimpleGUI as sg
from controller import windowController
from ref import MENU


menu_def = [['Arquivo', [MENU.OPEN, MENU.SAVE, MENU.DADOS, MENU.CLOSE]], ['Ajuda',[MENU.ABOUT]]]
layout = [[sg.Menu(menu_def)], [sg.Image(size=(800,800),key="display_img")]]

window = sg.Window("Proc. Image", layout, size=(800, 800), resizable=True)

winABOUT_activated = False

controller = windowController(window)

operacoes = {
    MENU.OPEN: controller.menu_open,
    MENU.ABOUT: controller.menu_about,
    MENU.SAVE: controller.save_file,
    MENU.DADOS: controller.get_dados
}

while True:
    event, values = window.read()
    
    if event == MENU.CLOSE or event == sg.WIN_CLOSED:
        break

    #Um "switch"                                                  
    operacoes[event]()

window.close()