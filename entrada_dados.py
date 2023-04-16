import PySimpleGUI as sg
import sqlite3
from contextlib import closing

def refresh_visualizacao_dados():

    with sqlite3.connect('laboratorio.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute("SELECT id, item FROM controle ORDER BY id")
            results = cursor.fetchall()
            return results



def frame_esquerdo():
    
    visualizar_resultado_esquerda = []
    resultado = refresh_visualizacao_dados()
    
    teste = int(len(resultado)/3)
    for i in range(0, teste):
        listaexames = resultado[i]

        visualizar_resultado_esquerda.append(
        [
            sg.Text(f'{listaexames[0]} - {listaexames[1]}'), sg.Push(), sg.Input(size=10, key=f'-item{i}-')
        ]
    )
    
    frame = [
        *visualizar_resultado_esquerda,
    ]
    return frame

def frame_central():
    
    visualizar_resultado_central = []
    resultado = refresh_visualizacao_dados()
    teste = int(len(resultado)/3)
    teste2 = teste * 2
    for i in range(teste, teste2):
        listaexames = resultado[i]
        
        visualizar_resultado_central.append(
        [
            sg.Text(f'{listaexames[0]} - {listaexames[1]}'), sg.Push(), sg.Input(size=10, key=f'-item{i}-')
        ]
    )   
    frame = [
        *visualizar_resultado_central,
    ]
    return frame
    

def frame_direito():
    visualizar_resultado_direita = []
    resultado = refresh_visualizacao_dados()
    if not resultado:
        return []
    teste = int(len(resultado)/3)
    teste2 = teste * 2
    for i in range(teste2, len(resultado)):
        listaexames = resultado[i]
        
        visualizar_resultado_direita.append(
        [
            sg.Text(f'{listaexames[0]} - {listaexames[1]}'), sg.Push(), sg.Input(size=10, key=f'-item{i}-')
        ]
    )   
    frame = [
        *visualizar_resultado_direita,
    ]
    return frame

def create_entrada_window(title=None, theme="DarkTeal6", location=(None, None)):
    sg.theme(theme)
    ano = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto','setembro', 'outubro', 'novembro', 'dezembro']
    
    coluna_esquerda = [
        [
            sg.Frame('ID - ITEM', frame_esquerdo()),
        ],
    ] 
    
    coluna_central = [
        [
            sg.Frame('ID - ITEM', frame_central()),
        ]
    ]
    
    coluna_direita = [
        [
            sg.Frame('ID - ITEM', frame_direito()),
        ],
    ]
    
    layout = [
        [
            sg.Text('Escolha o Mês'),
            sg.Combo(values = ano, default_value = 'janeiro', enable_events=True, key= '-mes_selecionado-'),
                   
        ],
        [
            sg.Column(coluna_esquerda),sg.Column(coluna_central), sg.Column(coluna_direita)
        ],
        [
            sg.Button('Salvar',bind_return_key=True, key= '-confirmar_cadastro-'), sg.Button('Voltar', bind_return_key=True, key='-voltar_cadastro-')
        ]
    ]

    if title is None:
        title = "Visualizar Saldo"
    else:
        title = title
    
    window = sg.Window(title, layout, resizable=True, finalize=True, location=location, disable_close=True)
    
    # Feche a janela
    
    return window
