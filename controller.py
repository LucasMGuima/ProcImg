import PySimpleGUI as sg

from PIL import Image
from ref import MENU

import io

class windowController:
    def __init__(self, window: sg.Window) -> None:
        self.winABOUT_activated = False
        self.image = None

        self.window = window

    def resize_image(self, ImagePath):
        img = Image.open(ImagePath)
        img = img.resize((800,600), Image.Resampling.LANCZOS)
        return img

    def menu_open(self) -> None:
        filename =  sg.popup_get_file('Selecione uma imagem', file_types=(("Imagens", "*.jpg *.png *.jpeg"),))
        self.image = filename

        if filename:
            resized_img = self.resize_image(filename)

            img_bytes = io.BytesIO()
            resized_img.save(img_bytes, format='PNG')
            self.window["display_img"].update(data=img_bytes.getvalue())

    def menu_about(self) -> None:
        self.winABOUT_activated = True

        winABOUT_layout = [[sg.Text("Lucas da Mata"), sg.Button("Ok")]]
        winABOUT = sg.Window(MENU.ABOUT, winABOUT_layout, margins=(100, 100))
        winABOUT_event, winABOUT_values = winABOUT.read()
        
        if winABOUT_event == "Ok" or winABOUT_event == sg.WIN_CLOSED:
            self.winABOUT_activated = False
            winABOUT.Close()

    def get_dados(self) -> None:
        imagem = Image.open(self.image)
        
        dados = imagem._getexif()
        #34853 35000
        if dados:
            for key, val in dados.items():
                if key == 34853 or key == 35000:
                    #converte cord geografica para latitude/longitude
                    latitude = float(val[2][0] + (val[2][1]/60) + (val[2][2]/3600))
                    if val[1] == 'S':
                        latitude *= -1.0
                    
                    longitude = float(val[4][0] + (val[4][1]/60) + (val[4][2]/3600))
                    if val[3] == 'W':
                        longitude *= -1.0

                    maps = f"https://www.google.com.br/maps/@{latitude},{longitude},17z?entry=ttu"
                    sg.popup(maps, title="Local")


    def save_file(self) -> None:
        if self.image == None:
            print("Nenhuma imagem aberta")
            return


        if self.image:
            image_atual = Image.open(self.image)
            with open("imagemsalva.png", 'wb') as file:
                image_atual.save(file)