import PySimpleGUI as sg

from PIL import Image
from ref import MENU

import io

class windowController:
    def __init__(self, window: sg.Window) -> None:
        self.winABOUT_activated = False
        self.image = None

        self.window = window

    def resize_image(self) -> Image:
        """
            Redimensiona a imagem para o tamanho da janela atual.

            Retorna:\n
            imagem redimensionada no formato Image
        """
        img = self.image

        width, height = img.size
        ascpect_ratio = width/height

        new_width = self.window.get_screen_size()[0]
        new_heigth = int(new_width / ascpect_ratio)
        img = img.resize((new_width, new_heigth), Image.Resampling.LANCZOS)

        new_heigth = self.window.get_screen_size()[1]
        new_width = int(new_heigth * ascpect_ratio)
        img = img.resize((new_width, new_heigth), Image.Resampling.LANCZOS)

        return img

    def menu_open(self) -> None:
        """
            Carrega uma nova imagem dentro do programa.
        """
        filename =  sg.popup_get_file('Selecione uma imagem', file_types=(("Imagens", "*.jpg *.png *.jpeg"),))
        self.image = Image.open(filename)

        if filename:
            self.image = self.resize_image()
            self._show_image()

    def _show_image(self):
        """
            Mostra aimagem dentro do campo imagem
        """
        img_bytes = io.BytesIO()
        self.image.save(img_bytes, format='PNG')
        self.window["display_img"].update(data=img_bytes.getvalue())

    def menu_about(self) -> None:
        """
            Cria e mostra o menu sobre.
        """
        self.winABOUT_activated = True

        winABOUT_layout = [[sg.Text("Lucas da Mata"), sg.Button("Ok")]]
        winABOUT = sg.Window(MENU.ABOUT, winABOUT_layout, margins=(100, 100))
        winABOUT_event, winABOUT_values = winABOUT.read()
        
        if winABOUT_event == "Ok" or winABOUT_event == sg.WIN_CLOSED:
            self.winABOUT_activated = False
            winABOUT.Close()

    def get_dados(self) -> None:
        """
            Pega os dados da imagem.
        """
        imagem = self.image
        
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


    def apply_gray_scale(self) -> None:
        """
            Transforma a imagem para uma escala de cinza.
        """
        image = self.image
        if image:
            width, height = image.size
            pixels = image.load()
            previus_state = image.copy()

            for w in range(width):
                for h in range(height):
                    r, g, b = image.getpixel((w,h))
                    gray = int(0.3 * r + 0.6 * g + 0.1 * b)
                    pixels[w, h] = (gray, gray, gray)
            
            self._show_image()
        
    def apply_sepia(self) -> None:
        """
            Aplica um filtro de sepia a imagem.
        """
        image = self.image
        if image:
            width, height = image.size
            pixels = image.load()
            previus_state = image.copy()

            for w in range(width):
                for h in range(height):
                    r, g, b = image.getpixel((w,h))
                    gray = int(0.3 * r + 0.6 * g + 0.1 * b)
                    pixels[w, h] = (
                            gray+100 if gray+100 <= 255 else 255, 
                            gray+50 if gray+50 <= 255 else 255, 
                            gray
                        )
            
            self._show_image()
            
    def inverter_cor(self) -> None:
        """
            Inverte as cores atuais da imagem.
        """
        image = self.image
        if image:
            width, height = image.size
            pixels = image.load()
            previus_state = image.copy()

            for w in range(width):
                for h in range(height):
                    r, g, b = image.getpixel((w,h))
                    pixels[w, h] = (255 - r, 255 - g, 255 - b)
            
            self._show_image()


    def save_file(self) -> None:
        if self.image == None:
            print("Nenhuma imagem aberta")
            return


        if self.image:
            image_atual = self.image
            with open("imagemsalva.png", 'wb') as file:
                image_atual.save(file)