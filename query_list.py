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

# Query para gerar os arquivos xlsx que serão salvos, aqui resolvi usar pandas para ajudar na manipulação e geração dos arquivos xlsx
def gerar_arquivo():
    
    with sqlite3.connect('laboratorio.db') as conexao:
            
        query = 'SELECT sum(valor * janeiro) as Janeiro, sum(valor * fevereiro) as Fevereiro, sum(valor * março) as Março, sum(valor * abril) as Abril, sum(valor * maio) as Maio, sum(valor * junho) as Junho, sum(valor * julho) as Julho, sum(valor * agosto) as Agosto, sum(valor * setembro) as Setembro, sum(valor * outubro) as Outubro, sum(valor * novembro) as Novembro, sum(valor * dezembro) as Dezembro  FROM controle'
        
        df = pd.read_sql(query, conexao)

    df.to_excel('Fechamento.xlsx', index=False)

    with sqlite3.connect('laboratorio.db') as conexao:
        
        query = 'SELECT * FROM controle'
        
        df = pd.read_sql(query, conexao)
        
    df.to_excel('Controle.xlsx', index=False)