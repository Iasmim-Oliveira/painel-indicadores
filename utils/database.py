from sqlalchemy import create_engine
import pandas as pd
from urllib.parse import quote_plus

def conexao_banco(user, password, host, porta, banco_de_dados):
    senha_codificada = quote_plus(password)
    url_conexao = f'postgresql://{user}:{senha_codificada}@{host}:{porta}/{banco_de_dados}'
    engine = create_engine(url_conexao)
    return engine

def realizar_consulta(engine, consulta_sql):
    data_frame = pd.read_sql_query(consulta_sql, engine)
    return data_frame

def tratar_dados(data_frame):

    df_tratado = data_frame
    # Mapeamento dos números dos meses para os nomes dos meses em português
    meses_mapping = {
        1.0: 'Janeiro', 2.0: 'Fevereiro', 3.0: 'Março', 4.0: 'Abril',
        5.0: 'Maio', 6.0: 'Junho', 7.0: 'Julho', 8.0: 'Agosto',
        9.0: 'Setembro', 10.0: 'Outubro', 11.0: 'Novembro', 12.0: 'Dezembro'
    }

    # Substituindo os números dos meses pelos nomes em português
    df_tratado['mes'] = df_tratado['mes'].map(meses_mapping)

    # Convertendo a coluna area_influencia_mes para valores inteiros
    df_tratado['area_influencia_mes'] = df_tratado['area_influencia_mes'].astype(int)

    # Convertendo a coluna ano para inteiros para remover o ".0"
    df_tratado['ano'] = df_tratado['ano'].astype(int)

    # Ordenando o DataFrame pelos meses e ano
    meses_ordenados = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]
    df_tratado['mes'] = pd.Categorical(df_tratado['mes'], categories=meses_ordenados, ordered=True)
    df_tratado = df_tratado.sort_values(['mes', 'ano']).reset_index(drop=True)

    return df_tratado