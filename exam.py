import PySimpleGUI as sg

# Cria a janela principal
def create_exam_window(title=None, theme="DarkTeal6", size=(500, 200), location=(400, 270)):    
    # Definindo o nosso tema
    sg.theme(theme)

    # Definindo nosso layout
    layout = [
        [
            sg.Text("Exame:"),
            sg.Input(size=(30, 10), justification='left', key='-CADASTRO_EXAME-', focus=True)
        ],
        [
            sg.Text("Valor:   "),
            sg.Input(size=(20, 10), justification='left', default_text=0.0, key='-CADASTRO_VALOR-')
        ],
        [
            sg.Text("Saldo:  "),
            sg.Input(size=(20, 10), justification="left", default_text=0, key='-CADASTRO_SALDO-')
        ],
        [
            sg.Text()
        ],
        [],
        [
            sg.Button("Cadastrar", key="-CADASTRAR_EXAME-"),
            sg.Button('Voltar', key="-VOLTAR_EXAME-")
        ]
    ]
    
    # Definindo o titulo da janela
    if title is None:
        title = "Tela de Cadastro de Exame"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout, size=size, location=location, resizable=False, finalize=True, disable_close=True)
    
    # Retorna a nossa janela
    return window