import PySimpleGUI as sg
import sqlite3
from contextlib import closing

# Essa query foi criada aqui para possibilitar a atualização da sg.Table em tempo real
def refresh_visualizacao_window():
    
    with sqlite3.connect('laboratorio.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute("SELECT id, item, valor, saldo, janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro, restante, total FROM controle")
            results = cursor.fetchall()
            for i in results:
                # Refatorar? Talvez usando um looping?
                soma_saldo =  (i[4] + i[5] + i[6] + i[7] + i[8] + i[9] + i[10] + i[11] + i[12] + i[13] + i[14] + i[15])
                total_valor = soma_saldo * i[2]
                soma_saldo = i[3] - soma_saldo
                
                
                try:
                    cursor.execute(
                                '''
                                    UPDATE controle set restante = ?, total = ? WHERE id = ?
                                ''', (soma_saldo, total_valor, i[0])
                            )
                    conexao.commit()
                except:
                    conexao.rollback()
            cursor.execute("SELECT id, item, valor, saldo, janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro, restante, total FROM controle")
            results = cursor.fetchall()
            
            return results
    

def create_visualizacao_window(title=None, theme="DarkTeal6", size=(1200, 600)):
    sg.theme(theme)
    
    layout = [ 
            [
                sg.Text('LISTA DE EXAMES')
            ],
            [
               sg.Table(values=refresh_visualizacao_window(), headings=['Id', 'Exame', 'Valor', 'Saldo', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro', 'Saldo Restante', 'Total Gasto R$'], auto_size_columns=True, justification='center',vertical_scroll_only=False, alternating_row_color='blue', num_rows=min(25,25))
            ],
            [
                sg.Button('Voltar',key='-VOLTAR_VISUALIZAÇÃO-')
            ]
           
        ]
    if title is None:
        title = "Tela de Visualização de Dados de Exame"
    else:
        title = title
    
    window = sg.Window(title, layout, size= size, disable_close=True, resizable=True, finalize=True)
    # Feche a janela
    return window