import PySimpleGUI as sg

class windowController:
    def __init__(self, window: sg.Window) -> None:
        self.winABOUT_activated = False
        self.window = window

    def menu_open(self) -> None:
        filename = sg.popup_get_file('message will not be shown', no_window=True)
        self.window["display_img"].update(filename=filename, visible=True)
        self.window['display_img'].Position = (0,0)

    def menu_about(self) -> None:
        self.winABOUT_activated = True

        winABOUT_layout = [[sg.Text("Lucas da Mata"), sg.Button("Ok")]]
        winABOUT = sg.Window("About", winABOUT_layout, margins=(100, 100))
        winABOUT_event, winABOUT_values = winABOUT.read()
        
        if winABOUT_event == "Ok" or winABOUT_event == sg.WIN_CLOSED:
            self.winABOUT_activated = False
            winABOUT.Close()