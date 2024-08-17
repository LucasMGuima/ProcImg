import PySimpleGUI as sg
from controller import windowController

#Referencias de nome
MENU_CLOSE = "Close"
MENU_OPEN = "Open"
MENU_ABOUT = "About..."

menu_def = [['File', [MENU_OPEN, MENU_CLOSE]], ['Help',[MENU_ABOUT]]]
layout = [[sg.Menu(menu_def)], [sg.Image(pad=(0,0),key="display_img")]]

window = sg.Window("Proc. Image", layout, size=(700, 800))

winABOUT_activated = False

controller = windowController(window)

operacoes = {
    MENU_OPEN: controller.menu_open,
    MENU_ABOUT: controller.menu_about
}

while True:
    event, values = window.read()
    
    if event == MENU_CLOSE or event == sg.WIN_CLOSED:
        break

    operacoes[event]()