import PySimpleGUI as sg

def create_gui():
    layout = [
        [sg.Text("URL da Página"), sg.InputText(key="-URL-")],
        [sg.Button("Scrape and Save")],
    ]

    return sg.Window("Web Scraping com Python", layout, finalize=True)
