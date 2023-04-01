# Importando os pacotes e funções necessárias
import PySimpleGUI as sg
from view import create_main_window
from exam import create_exam_window
from manutencao import create_manu_window
from entrada_dados import create_entrada_window





if __name__ == "__main__":
    
    # Definindo a janela inicial
    window = create_main_window()
    
    while True:
        
        # Coletar Eventos e Valores atuais
        event, values = window.read()
        
        # Cancelar o loop ao fechar a janela
        if event == sg.WIN_CLOSED:
            break
    
    # Encerrar a janela
    window.close()