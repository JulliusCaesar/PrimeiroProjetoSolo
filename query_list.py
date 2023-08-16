import sqlite3
from contextlib import closing
import PySimpleGUI as sg
import pandas as pd


# Query para cadastrar um novo exame no sistema, recebendo os parâmetros que são passados pela tela de exam
def cadastro_exames(exame, valor, saldo):
    dados = [exame, valor, saldo]
    with sqlite3.connect('laboratorio.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            try: # Try para validar as informações recebidas
                cursor.execute(
                    '''
                        insert into controle (item, valor, saldo) values (?, ?, ?)
                    ''', dados
                )
                sg.popup('---- Exame cadastrado no Sistema ----', title='Atenção! ')
                conexao.commit()
            except sqlite3.IntegrityError: 
                # Esse é o punico erro que pode acontecer, pois somente não conseguira cadastrar um exame, caso o nome já esteja cadastrado
                sg.popup_cancel('------ Exame já existe no sistema ------', title="ATENÇÃO!")
                return False

# Query para realizar as pesuisas dos exames cadastrados, tanto por ID quanto por Nome de exame
def pesquisa_id(dado_pesquisa):
    with sqlite3.connect('laboratorio.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            
            cursor.execute(
                '''
                    SELECT * FROM controle WHERE id = ?
                ''',(dado_pesquisa,)
            )
            resultado = cursor.fetchone()
            conexao.commit()
            return resultado   
            

def pesquisa_exame(dado_pesquisa):
    with sqlite3.connect('laboratorio.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            
            cursor.execute(
                '''
                    SELECT * FROM controle WHERE item = ?
                ''',(dado_pesquisa,)
            )
            resultado = cursor.fetchone()
            conexao.commit()
            return resultado
            
# Query para atualizar os cadastros de qualquer exame no BD
def atualizar_exame(item, valor, saldo, id):
    valores_para_atualizar = [item, valor, saldo, id]
    with sqlite3.connect('laboratorio.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            try: 
                cursor.execute('UPDATE controle SET item = ?, valor = ?, saldo = ? WHERE id = ?', valores_para_atualizar)
                conexao.commit() 
            except:
                conexao.rollback()

# Query para gerar o arquivo xlsx que será salvo, aqui resolvi usar pandas para ajudar na manipulação e geração dos arquivos xlsx
def gerar_arquivo():
    
    with sqlite3.connect('laboratorio.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('SELECT * FROM controle')
            query = 'SELECT * FROM controle'
            resultado = cursor.fetchall()
            df = pd.read_sql(query, conexao)
    
    soma_janeiro = 0
    soma_fevereiro = 0
    soma_marco = 0
    soma_abril = 0
    soma_maio = 0
    soma_junho = 0
    soma_julho = 0
    soma_agosto = 0
    soma_setembro = 0
    soma_outubro = 0
    soma_novembro = 0
    soma_dezembro = 0
    
    id_len = len(df['id']) + 1
    for i in df['id']:
        soma_janeiro += df['valor'][i - 1] * df['janeiro'][i - 1]
        soma_fevereiro += df['valor'][i - 1] * df['fevereiro'][i - 1]
        soma_marco += df['valor'][i - 1] * df['março'][i - 1]
        soma_abril += df['valor'][i - 1] * df['abril'][i - 1]
        soma_maio += df['valor'][i - 1] * df['maio'][i - 1]
        soma_junho += df['valor'][i - 1] * df['junho'][i - 1]
        soma_julho += df['valor'][i - 1] * df['julho'][i - 1]
        soma_agosto += df['valor'][i - 1] * df['agosto'][i - 1]
        soma_setembro += df['valor'][i - 1] * df['setembro'][i - 1]
        soma_outubro += df['valor'][i - 1] * df['outubro'][i - 1]
        soma_novembro += df['valor'][i - 1] * df['novembro'][i - 1]
        soma_dezembro += df['valor'][i - 1] * df['dezembro'][i - 1]
    
    frame = [id_len,'','','Total', soma_janeiro, soma_fevereiro, soma_marco, soma_abril, soma_maio, soma_junho, soma_julho, soma_agosto, soma_setembro, soma_outubro, soma_novembro, soma_dezembro]
    resultado.append(frame)
    
    df2 = pd.DataFrame(resultado)
    df2.columns = ['Id', 'Item', 'Saldo', 'Valor', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro', 'Saldo Restante', 'Total']
    df2.to_excel('Resultado.xlsx', index=False)