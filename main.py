import PySimpleGUI as sg
from controller import windowController
from ref import MENU


menu_def = [['Arquivo', [MENU.OPEN, MENU.SAVE, MENU.DADOS, MENU.CLOSE]], 
            ['Ferramenta', [MENU.GRAY, MENU.SEPIA, MENU.INVERTER, MENU.CONVERT4COR, MENU.BLUR]], 
            ['Ajuda',[MENU.ABOUT]]]
layout = [[sg.Menu(menu_def)], [sg.Image(size=(800,600),key="display_img")]]

window = sg.Window("Proc. Image", layout, size=(800, 600), resizable=True)

winABOUT_activated = False

controller = windowController(window)

operacoes = {
    MENU.OPEN: controller.menu_open,
    MENU.ABOUT: controller.menu_about,
    MENU.SAVE: controller.save_file,
    MENU.DADOS: controller.get_dados,
    MENU.GRAY: controller.apply_gray_scale,
    MENU.SEPIA: controller.apply_sepia,
    MENU.INVERTER: controller.inverter_cor,
    MENU.CONVERT4COR: controller.apply_four_bits_filter,
    MENU.BLUR: controller.apply_blur
}

while True:
    event, values = window.read()
    
    if event == MENU.CLOSE or event == sg.WIN_CLOSED:
        break
  
    try:                                               
        #Um "switch"
        operacoes[event]()
    except:
        sg.popup("Nenhuma imagem encontrada")

window.close()