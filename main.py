import PySimpleGUI as sg

#Referencias de nome
MENU_CLOSE = "Close"
MENU_OPEN = "Open"
MENU_ABOUT = "About..."

menu_def = [['File', [MENU_OPEN, MENU_CLOSE]], ['Help',[MENU_ABOUT]]]
layout = [[sg.Menu(menu_def)]]

window = sg.Window("Proc. Image", layout, margins=(500, 400))

winABOUT_activated = False

while True:
    event, values = window.read()

    if event == MENU_ABOUT and not winABOUT_activated:
        winABOUT_activated = True

        winABOUT_layout = [[sg.Text("Lucas da Mata"), sg.Button("Ok")]]
        winABOUT = sg.Window(MENU_ABOUT, winABOUT_layout, margins=(100, 100))
        winABOUT_event, winABOUT_values = winABOUT.read()

        print(winABOUT_event)

        if winABOUT_event == "Ok" or winABOUT_event == sg.WIN_CLOSED:
            winABOUT_activated = False
            winABOUT.Close()
    if event == MENU_CLOSE or event == sg.WIN_CLOSED:
        break