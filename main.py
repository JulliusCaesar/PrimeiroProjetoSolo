# Importando os pacotes e funções necessárias
import PySimpleGUI as sg
from view import create_main_window
from exam import create_exam_window
from manutencao import create_manu_window
from entrada_dados import create_entrada_window
from query_list import cadastro_exames





if __name__ == "__main__":
    
    # Definindo a janela inicial
    window = create_main_window()
    
    while True:
        
        # Coletar Eventos e Valores atuais
        event, values = window.read()
        
        # Cancelar o loop ao fechar a janela
        if event == sg.WIN_CLOSED:
            break
        
        # Usando o event para ultilizar a tela cadastro exames
        elif "::cadastro_exame" in event:
            window.close()
            window = create_exam_window()
        
        elif event == "-CADASTRAR_EXAME-":
            
            cadastro_exame = str(values['-CADASTRO_EXAME-']).upper() # Pegando o valor contido no input e deixando em caixa alta e armazenando numa variável
            while True: # Utilizando um loop para validação de entrada de dados
                try:
                    cadastro_valor = float(values['-CADASTRO_VALOR-'].replace(',', '.'))
                    break
                except: # Exceção criada para caso o usuário não digite os valores corretos
                    cadastro_valor = sg.popup_get_text("Digite somente números para o VALOR DO EXAME", title="ATENÇÃO").replace(',', '.')
                    window['-CADASTRO_VALOR-'].update(cadastro_valor)
                    values['-CADASTRO_VALOR-'] = cadastro_valor
            
            while True: # Utilizando um loop para validação de entrada de dados
                try:
                    cadastro_saldo = int(values['-CADASTRO_SALDO-'])
                    break
                except: # Exceção criada para caso o usuário não digite os valores corretos
                    cadastro_saldo = sg.popup_get_text("Digite somente Números INTEIROS sem ponto ou virgula para o Saldo do exame      :", title="ATENÇÃO!")
                    window['-CADASTRO_SALDO-'].update(cadastro_saldo)
                    values['-CADASTRO_SALDO-'] = cadastro_saldo
            
            if cadastro_exames(cadastro_exame, cadastro_valor, cadastro_saldo) == False:
                window['-CADASTRO_EXAME-'].update('')
                window['-CADASTRO_EXAME-'].set_focus()
                window['-CADASTRO_VALOR-'].update(0.00)
                window['-CADASTRO_SALDO-'].update(0)
            else:
                window['-CADASTRO_EXAME-'].update('')
                window['-CADASTRO_EXAME-'].set_focus()
                window['-CADASTRO_VALOR-'].update(0.00)
                window['-CADASTRO_SALDO-'].update(0)
                
    
    # Encerrar a janela
    window.close()