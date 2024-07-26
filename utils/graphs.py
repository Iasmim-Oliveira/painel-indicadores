import plotly.graph_objects as go
import pandas as pd

# Gráfico de Linhas
def gerar_grafico_linhas(df_tratado):
    data_frame = df_tratado

    # Ordenar os meses
    ordem_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    data_frame['mes'] = pd.Categorical(data_frame['mes'], categories=ordem_meses, ordered=True)

    # Definir as cores para cada ano
    cores = {2021: '#1f77b4', 2022: '#ff7f0e', 2023: '#2ca02c', 2024: '#c73b20'}

    # Criar a figura
    fig_linhas = go.Figure()

    # Adicionar uma linha para cada ano
    for ano in data_frame['ano'].unique():
        df_ano = data_frame[data_frame['ano'] == ano]
        fig_linhas.add_trace(go.Scatter(
            x=df_ano['mes'],
            y=df_ano['area_influencia_mes'],
            name=str(ano),
            line=dict(color=cores[int(ano)], width=3)
        ))

    # Calcular média, mínimo e máximo da área queimada total
    total_area_queimada = data_frame['area_influencia_mes'].sum()
    media_total = total_area_queimada / len(data_frame)
    minimo_total = data_frame['area_influencia_mes'].min()
    maximo_total = data_frame['area_influencia_mes'].max()

    # Adicionar linhas de média, mínimo e máximo
    fig_linhas.add_trace(go.Scatter(
        x=ordem_meses,
        y=[int(media_total)] * len(ordem_meses),
        mode='lines',
        name='Média',
        line=dict(color='#e377c2', dash='dash')
    ))
    fig_linhas.add_trace(go.Scatter(
        x=ordem_meses,
        y=[int(minimo_total)] * len(ordem_meses),
        mode='lines',
        name='Mínimo',
        line=dict(color='#9467bd', dash='dash')
    ))
    fig_linhas.add_trace(go.Scatter(
        x=ordem_meses,
        y=[int(maximo_total)] * len(ordem_meses),
        mode='lines',
        name='Máximo',
        line=dict(color='#8c564b', dash='dash')
    ))

    # Atualizar layout
    fig_linhas.update_layout(
        barmode='group',  # Usado para agrupar as barras
        legend_title='Anos'
    )

    # Atualizar layout
    fig_linhas.update_layout(
        title=dict(
            text='Gráfico em Linhas da Área Queimada no Mês por Ano',
            font=dict(
                family='Arial, sans-serif',
                size=20,
                color='black',
                weight='bold'
            )
        ),
        xaxis_title='Mês',
        yaxis_title='Área Queimada (Mês)',
        legend_title=dict(
            text='Anos',
            font=dict(
                family='Arial, sans-serif',
                size=16,
                color='black',
                weight='bold'
            )
        ),
        xaxis=dict(
            tickfont=dict(
                family='Arial, sans-serif',
                size=14,
                color='black',
                weight ='bold'
            ),
            titlefont=dict(
                family='Arial, sans-serif',
                size=16,
                color='black',
                weight='bold'
            )
        ),
        yaxis=dict(
            dtick=30000, # Definido o intervalo do eixo y para 20.000 unidades
            tickformat=',',  # Formatando os valores para milhares
            tickfont=dict(
                family='Arial, sans-serif',
                size=14,
                color='black',
                weight ='bold'
            ),
            titlefont=dict(
                family='Arial, sans-serif',
                size=16,
                color='black',
                weight ='bold'
            )
        ),
        title_x=0.5,  # Centraliza o título
        template='presentation',
    )

    return fig_linhas

# Gráfico de Barras
def gerar_grafico_barras(df_tratado):
    data_frame = df_tratado

    # Ordenar os meses
    ordem_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    data_frame['mes'] = pd.Categorical(data_frame['mes'], categories=ordem_meses, ordered=True)

    # Definir as cores para cada ano
    cores = {2021: '#1f77b4', 2022: '#ff7f0e', 2023: '#2ca02c', 2024: '#c73b20'}

    # Criar a figura
    fig_barras = go.Figure()

    # Adicionar uma linha para cada ano
    for ano in data_frame['ano'].unique():
        df_ano = data_frame[data_frame['ano'] == ano]
        fig_barras.add_trace(go.Bar(
            x=df_ano['mes'],
            y=df_ano['area_influencia_mes'],
            name=str(ano),
            marker_color=cores[int(ano)]
        ))

    # Calcular média, mínimo e máximo da área queimada total
    total_area_queimada = data_frame['area_influencia_mes'].sum()
    media_total = total_area_queimada / len(data_frame)
    minimo_total = data_frame['area_influencia_mes'].min()
    maximo_total = data_frame['area_influencia_mes'].max()

    # Adicionar linhas de média, mínimo e máximo
    fig_barras.add_trace(go.Scatter(
        x=ordem_meses,
        y=[int(media_total)] * len(ordem_meses),
        mode='lines',
        name='Média',
        line=dict(color='#e377c2', dash='dash')
    ))

    fig_barras.add_trace(go.Scatter(
        x=ordem_meses,
        y=[int(minimo_total)] * len(ordem_meses),
        mode='lines',
        name='Mínimo',
        line=dict(color='#9467bd', dash='dash')
    ))

    fig_barras.add_trace(go.Scatter(
        x=ordem_meses,
        y=[int(maximo_total)] * len(ordem_meses),
        mode='lines',
        name='Máximo',
        line=dict(color='#8c564b', dash='dash')
    ))

    # Atualizar layout
    fig_barras.update_layout(
        barmode='group',  # Usado para agrupar as barras
        legend_title='Anos'
    )

    # Atualizar layout
    fig_barras.update_layout(
        title=dict(
            text='Gráfico em Barras da Área Queimada no Mês por Ano',
            font=dict(
                family='Arial, sans-serif',
                size=20,
                color='black',
                weight='bold'
            )
        ),
        xaxis_title='Mês',
        yaxis_title='Área Queimada (Mês)',
        legend_title=dict(
            text='Anos',
            font=dict(
                family='Arial, sans-serif',
                size=16,
                color='black',
                weight='bold'
            )
        ),
        xaxis=dict(
            tickfont=dict(
                family='Arial, sans-serif',
                size=14,
                color='black',
                weight ='bold'
            ),
            titlefont=dict(
                family='Arial, sans-serif',
                size=16,
                color='black',
                weight='bold'
            )
        ),
        yaxis=dict(
            dtick=30000, # Definido o intervalo do eixo y para 20.000 unidades
            tickformat=',',  # Formatando os valores para milhares
            tickfont=dict(
                family='Arial, sans-serif',
                size=14,
                color='black',
                weight ='bold'
            ),
            titlefont=dict(
                family='Arial, sans-serif',
                size=16,
                color='black',
                weight ='bold'
            )
        ),
        title_x=0.5,  # Centraliza o título
        template='presentation'
    )


    return fig_barras

# Valores em Tabela
def gerar_tabela(df_tratado):
    data_frame = df_tratado

    # Renomear as colunas
    data_frame = data_frame.rename(columns={
        'mes': 'Mês',
        'ano': 'Ano',
        'area_influencia_mes': 'Área de Influência (km²)',
        'qtd_eventos': 'Quantidade de Eventos',
        'qtd_focos': 'Quantidade de Focos'
    })

    # Adicionar "km²" aos valores da coluna "Área Queimada (km²)"
    data_frame['Área de Influência (km²)'] = data_frame['Área de Influência (km²)'].astype(str) + ' km²'
    
    tabela = go.Figure(data=[go.Table(
        header=dict(
            values=list(data_frame.columns),
            fill_color='#c73b20',
            align='center',
            font=dict(
                family='Arial, sans-serif',
                size=20,
                color='white',
                weight='bold'
            ),
            line_color='black',  # Cor da borda das células
            line_width=1  # Largura da borda das células
        ),
        cells=dict(
            values=[data_frame[col] for col in data_frame.columns],
            fill_color='#fcf6e2',
            align='center',
            font=dict(
                family='Arial, sans-serif',
                size=18,
                color='black',
                weight='bold'
            ),
            line_color='black',  # Cor da borda das células
            line_width=1,  # Largura da borda das células
            height=30
        )
    )])

    tamanho_tabela = len(data_frame) / 2
    # Atualiza o layout da tabela
    tabela.update_layout(
        title=dict(
            text='Tabela de Área Queimada no Mês por Ano',
            font=dict(
                family='Arial, sans-serif',
                size=20,
                color='black',
                weight='bold'
            )
        ),
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=10),
        height=len(data_frame) * tamanho_tabela + 100,  # Ajusta a altura com base no número de linhas
        title_x=0.5, # Centraliza o título
    )

    return tabela