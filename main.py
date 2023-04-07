# Importando os pacotes e funções necessárias
import PySimpleGUI as sg
from view import create_main_window
from exam import create_exam_window
from manutencao import create_manu_window
from entrada_dados import create_entrada_window
from visualizacao import create_visualizacao_window
from query_list_mes import refresh_dados_mes, exames_mes_escolhido
from query_list import cadastro_exames, pesquisa_id, pesquisa_exame, atualizar_exame





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
                
        elif event == "-VOLTAR_EXAME-":
            window.close()
            window = create_main_window()
        
        # Usando o event para ultilizar a tela de masnutenção de exames
        elif '::manutenção_exame' in event:
            window.close()
            window = create_manu_window()
        
        # Evento utilizado para definir por onde será relizado a pesquisa, se por ID ou por Nome de Exame
        elif event == "-PESQUISAR_POR_ID-" and values["-PESQUISAR_POR_ID-"] == True:
            window['-PROCURAR_ID-'].update(readonly=False)
            window['-MANUTENÇÃO_EXAME-'].update(readonly=True)
            window['-MANUTENÇÃO_VALOR-'].update(readonly=True)
            window['-MANUTENÇÃO_SALDO-'].update(readonly=True)
            window['-PESQUISAR_EXAME-'].update(visible=False)
            window['-PESQUISAR_ID-'].update(visible=True)
        
        elif event == "-PESQUISA_POR_EXAME-" and values["-PESQUISA_POR_EXAME-"] == True:
            window['-PROCURAR_ID-'].update(readonly=True)
            window['-MANUTENÇÃO_EXAME-'].update(readonly=False)
            window['-MANUTENÇÃO_VALOR-'].update(readonly=True)
            window['-MANUTENÇÃO_SALDO-'].update(readonly=True)
            window['-PESQUISAR_ID-'].update(visible=False)
            window['-PESQUISAR_EXAME-'].update(visible=True)
        
        # Evento que usa as informações de ID para pesquisar no BD
        elif event == '-PESQUISAR_ID-':
            try:
                id_pesquisa = int(values['-PROCURAR_ID-'])
            except:
                id_pesquisa = int(sg.popup_get_text("Digite somente Números INTEIROS sem ponto e virgula:", title="ATENÇÃO!"))
                window['-PROCURAR_ID-'].update(id_pesquisa)
            
            resultado_id = pesquisa_id(id_pesquisa)
            if resultado_id == None:
                sg.popup_error('Exame não cadastrado', title="ATENÇÃO!")
            else:
                window['-MANUTENÇÃO_EXAME-'].update(resultado_id[1])
                window['-MANUTENÇÃO_VALOR-'].update(resultado_id[2])
                window['-MANUTENÇÃO_SALDO-'].update(resultado_id[3])
                window['-MANUTENÇÃO_EXAME-'].update(readonly=False)
                window['-MANUTENÇÃO_VALOR-'].update(readonly=False)
                window['-MANUTENÇÃO_SALDO-'].update(readonly=False)
        
        elif event == "-PESQUISAR_EXAME-":
                
            exame_pesquisa = str(values['-MANUTENÇÃO_EXAME-']).upper()            
            resultado_exame = pesquisa_exame(exame_pesquisa)
            if resultado_exame == None:
                sg.popup_error('Exame não cadastrado', title="ATENÇÃO!")
                
            else:
                window['-PROCURAR_ID-'].update(resultado_exame[0])
                window['-MANUTENÇÃO_VALOR-'].update(resultado_exame[2])
                window['-MANUTENÇÃO_SALDO-'].update(resultado_exame[3])
                window['-MANUTENÇÃO_VALOR-'].update(readonly=False)
                window['-MANUTENÇÃO_SALDO-'].update(readonly=False)
        
        elif event == '-SALVAR_EXAME-':
            confirmar = sg.popup_ok_cancel('Tem certeza que deseja alterar as informações?', title="ATENÇÃO!")
            if confirmar == 'OK':
                atualizar_exame(values['-MANUTENÇÃO_EXAME-'].upper(), values['-MANUTENÇÃO_VALOR-'].replace(',','.'), values['-MANUTENÇÃO_SALDO-'], values['-PROCURAR_ID-'],)
            
            window.close()
            window = create_main_window()
        
        elif event == '-VOLTAR_MANUTENCAO-':
            window.close()
            window = create_main_window()
        
        elif '::visalizar_exames' in event:
            window.close()
            window = create_visualizacao_window()
        
        elif event == '-VOLTAR_VISUALIZAÇÃO-':
            window.close()
            window = create_main_window()
        
        elif "::utilizado" in event:
            window.close()
            window = create_entrada_window()
        
        elif event == '-mes_selecionado-':
            mes_selecionado = refresh_dados_mes(values['-mes_selecionado-'])
            for i in range (len(mes_selecionado)):
                window[f'-item{i}-'].update(mes_selecionado[i][1])
            
        elif event == '-confirmar_cadastro-':
            entrada_saldo = []
            for count in values:
                if values[count] in ['janeiro', 'fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']:
                    entrada_saldo.append(values[count])
                else:
                    try:
                        entrada_saldo.append(int(values[count]))
                    except:
                        sg.popup_error('Digite somente Números Inteiros sem ponto ou virgula!', title="ATENÇÃO!")
            print(entrada_saldo)
            exames_mes_escolhido(entrada_saldo)
            
        elif event == '-voltar_cadastro-':
            window.close()
            window = create_main_window()
            
        elif "::version" in event:
            sg.popup("=== Versão do sistema 1.0.0 ===\n=== Autor: Júlio César ===", title="Créditos")
            
    # Encerrar a janela
    window.close()