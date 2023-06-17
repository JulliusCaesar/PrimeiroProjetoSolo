import PySimpleGUI as sg



# Cria a janela principal
def create_manu_window(title=None, theme="DarkTeal6", size=(500, 220), font=("Arial", 10), location=(None, None)):    
    # Definindo o nosso tema
    sg.theme(theme)

    # Definindo nosso layout
    layout = [
        [
            sg.Radio('ID', group_id='pesquisa',enable_events=True, key='-PESQUISAR_POR_ID-'),
            sg.Radio('EXAME',group_id='pesquisa', enable_events=True, key='-PESQUISA_POR_EXAME-')
        ],
        [
            sg.Text('ID:'),
            sg.Input(size=(30, 10), justification='left', key='-PROCURAR_ID-', readonly=True),
            sg.Button('Pesquisar', visible=False, key='-PESQUISAR_ID-')
        ],
        [
            sg.Text("Exame:"),
            sg.Input(size=(30, 10), justification='left',key='-MANUTENÇÃO_EXAME-', readonly=True),
            sg.Button('Pesquisar', visible=False, key='-PESQUISAR_EXAME-')
        ],
        [
            sg.Text("Valor:"),
            sg.Input(size=(20, 10), justification='left',key='-MANUTENÇÃO_VALOR-', readonly=True)
        ],
        [
            sg.Text("Saldo:"),
            sg.Input(size=(20, 10), justification="left", key='-MANUTENÇÃO_SALDO-', readonly=True)
        ],
        [
            sg.Text()
        ],
        [],
        [
            sg.Button("Salvar", key="-SALVAR_EXAME-"),
            sg.Button('Voltar', key="-VOLTAR_MANUTENCAO-")
        ]
    ]
    
    # Definindo o titulo da janela
    if title is None:
        title = "Tela de Manutenção de Exame"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout, size=size, location=location, font=font, resizable=False, finalize=True, disable_close=True)
    
    # Retorna a nossa janela
    return window 