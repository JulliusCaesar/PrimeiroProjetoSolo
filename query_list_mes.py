import sqlite3
from contextlib import closing

# Decidi fazer essas query separadas para facilitar a manutenção futuramente

# Essa query cadastra as informações em cada Mes
def exames_mes_escolhido(dados):
    saldo_exames = []
    if dados[0] == 'janeiro':
        for i in dados:
            if i == 'janeiro':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set janeiro = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'fevereiro':
        for i in dados:
            if i == 'fevereiro':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set fevereiro = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'março':
        for i in dados:
            if i == 'março':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set março = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'abril':
        for i in dados:
            if i == 'abril':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set abril = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'maio':
        for i in dados:
            if i == 'maio':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set maio = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'junho':
        for i in dados:
            if i == 'junho':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set junho = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'julho':
        for i in dados:
            if i == 'julho':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set julho = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'agosto':
        for i in dados:
            if i == 'agosto':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set agosto = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'setembro':
        for i in dados:
            if i == 'setembro':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set setembro = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'outubro':
        for i in dados:
            if i == 'outubro':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set outubro = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'novembro':
        for i in dados:
            if i == 'novembro':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set novembro = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'dezembro':
        for i in dados:
            if i == 'dezembro':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set dezembro = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
                        

# Query que puxa as informações de cada Mês

def exames_mes_escolhido(dados):
    saldo_exames = []
    if dados[0] == 'janeiro':
        for i in dados:
            if i == 'janeiro':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set janeiro = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'fevereiro':
        for i in dados:
            if i == 'fevereiro':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set fevereiro = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'março':
        for i in dados:
            if i == 'março':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set março = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'abril':
        for i in dados:
            if i == 'abril':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set abril = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'maio':
        for i in dados:
            if i == 'maio':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set maio = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'junho':
        for i in dados:
            if i == 'junho':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set junho = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'julho':
        for i in dados:
            if i == 'julho':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set julho = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'agosto':
        for i in dados:
            if i == 'agosto':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set agosto = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'setembro':
        for i in dados:
            if i == 'setembro':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set setembro = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'outubro':
        for i in dados:
            if i == 'outubro':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set outubro = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'novembro':
        for i in dados:
            if i == 'novembro':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set novembro = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()
    elif dados[0] == 'dezembro':
        for i in dados:
            if i == 'dezembro':
                pass
            else:
                saldo_exames.append(int(i))
        with sqlite3.connect('laboratorio.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                contador = 1
                for saldo in saldo_exames:
                    try:
                        cursor.execute('''
                                        update controle set dezembro = ? where id = ?                    
                                        ''',(saldo, contador)
                                        )
                        contador += 1
                        conexao.commit()
                    except:
                        conexao.rollback()