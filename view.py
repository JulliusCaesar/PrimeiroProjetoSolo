import PySimpleGUI as sg
import sqlite3
from contextlib import closing

# Menu bar principal
def menu_bar():
    menu = [
        [
            "   &Exames     ",
            ["&Cadastro de Exames::cadastro_exame", "&Manutenção de Exames::manutenção_exame", "&Visualizar Exames::visalizar_exames"],
        ],
        [
            "   S&aldo      ",
            ['&Cadastro de Saldo::utilizado'],
        ],
        [
             "&Sobre",
            ["&Créditos::credits", "&Versão::version"],
        ]
    ]
    return menu

# Criar a janela principal
def create_main_window(title=None, theme="DarkTeal6", size=(1100, 500), font=("Arial", 10), location=(None, None)):
    # Definindo o tema
    sg.theme(theme)
    
    # Criando o banco de dados e o acessando, cria tabém a tabela caso não exista
    with sqlite3.connect('laboratorio.db') as conexao:
        conexao.row_factory = sqlite3.Row
        with closing(conexao.cursor()) as cursor:
            cursor.execute(
                '''
                    create table if not exists controle(
                        id integer not null primary key autoincrement,
                        item text unique,
                        valor float default 0,
                        saldo integer default 0,
                        janeiro integer default 0,
                        fevereiro integer default 0,
                        março integer default 0,
                        abril integer default 0,
                        maio integer default 0,
                        junho integer default 0,
                        julho integer default 0,
                        agosto integer default 0,
                        setembro integer default 0,
                        outubro integer default 0,
                        novembro integer default 0,
                        dezembro integer default 0,
                        restante integer,
                        total float
                    )
                '''
            )
            
    # Definindo o layout
    layout = [
        [
            sg.MenubarCustom(menu_bar(), bar_font=("Arial", 25), font=('Arial', 10))
        ],
        [
            sg.Text('CONTROLE DE SALDO E VALORES DO LABORATÓRIO VALE DIAGNÓSTICOS', size=(400,200), text_color='black',justification='center',font=('Arial', 20))
        ]
    ]
    
    # Definindo o titulo da Janela
    if title is None:
        title = "Menu"
    else:
        title = title
    
    # Criando a janela e deixando ela finalizavel
    window = sg.Window(title, layout, size=size, location=location, resizable=False, finalize=True)
    
    return window