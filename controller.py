import PySimpleGUI as sg

from PIL import Image
from ref import MENU

class windowController:
    def __init__(self, window: sg.Window) -> None:
        self.winABOUT_activated = False
        self.image = None

        self.window = window

    def menu_open(self) -> None:
        filename = sg.popup_get_file('message will not be shown', no_window=True)
        self.image = filename
        
        if ".jpg" in self.image:
            sg.popup_notify(title="Erro", message="Não é possivél abrir arquivos do tipo JPG")
            return
        
        self.window["display_img"].update(filename=filename, visible=True)
        self.window['display_img'].Position = (0,0)

    def menu_about(self) -> None:
        self.winABOUT_activated = True

        winABOUT_layout = [[sg.Text("Lucas da Mata"), sg.Button("Ok")]]
        winABOUT = sg.Window(MENU.ABOUT, winABOUT_layout, margins=(100, 100))
        winABOUT_event, winABOUT_values = winABOUT.read()
        
        if winABOUT_event == "Ok" or winABOUT_event == sg.WIN_CLOSED:
            self.winABOUT_activated = False
            winABOUT.Close()

    def save_file(self) -> None:
        if self.image == None:
            print("Nenhuma imagem aberta")
            return

        #Tenta carregar a imagem
        try:
            img = Image.open(self.image)
            filename = self.image.split('.')[0]
        except:
            print("Não foi possivel carregar a imagem")
            return
        
        #Tenta salvar a imagem
        image_name = self.image.split('.')[0].split('/')[-1]
        name = sg.popup_get_text('File name: ', default_text=image_name)
        
        try:
            outfile = filename + '.jpg'
            img.save(outfile)
        except:
            print("Não foi possivel salvar a imagem")