import PySimpleGUI as sg
from scraper import scrape_and_save_data
from ui.gui import create_gui

if __name__ == "__main__":
    sg.theme("LightGrey1")
    
    # Crie a interface gráfica
    window = create_gui()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Scrape and Save":
            url = values["-URL-"]
            success = scrape_and_save_data(url)
            if success:
                sg.popup("Texto salvo no banco de dados com sucesso!", title="Sucesso")
            else:
                sg.popup("Erro ao salvar o texto no banco de dados.", title="Erro")

    window.close()
