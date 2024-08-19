import PySimpleGUI as sg
from controller import windowController
from ref import MENU


menu_def = [['File', [MENU.OPEN, MENU.SAVE, MENU.CLOSE]], ['Help',[MENU.ABOUT]]]
layout = [[sg.Menu(menu_def)], [sg.Image(pad=(0,0),key="display_img")]]

window = sg.Window("Proc. Image", layout, size=(700, 800))

winABOUT_activated = False

controller = windowController(window)

operacoes = {
    MENU.OPEN: controller.menu_open,
    MENU.ABOUT: controller.menu_about,
    MENU.SAVE: controller.save_file
}

while True:
    event, values = window.read()
    
    if event == MENU.CLOSE or event == sg.WIN_CLOSED:
        break

    #Um "switch"
    try:
        operacoes[event]()
    except:
        print("Ainda não implementado")