from flask import Flask, request, render_template, jsonify
from utils.graphs import gerar_grafico_barras, gerar_grafico_linhas, gerar_tabela
from utils.database import conexao_banco, realizar_consulta, tratar_dados
from utils.filters import aplicar_filtros

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/filtrar', methods=['POST'])
def filtrar():

    if not request.is_json:
        return "Unsupported Media Type", 415
    
    filtros = request.get_json()

    # Debugar
    print(filtros)
    consulta_sql = aplicar_filtros(filtros)
    # Debugar
    print("Consulta SQL:", consulta_sql)
    engine = conexao_banco('USER', 'PASSWORD', 'IPBANCO', 'PORTBANCO', 'NAMEBANCO')
    data_frame = realizar_consulta(engine, consulta_sql) 
    # Debugar   
    print("DataFrame:", data_frame)
    dados_tratados = tratar_dados(data_frame)
    # Debugar
    print("Dados Tratados:", dados_tratados)

    grafico_linhas = gerar_grafico_linhas(dados_tratados)
    grafico_linhas_html = grafico_linhas.to_html(full_html=False)
    grafico_barras = gerar_grafico_barras(dados_tratados)
    grafico_barras_html = grafico_barras.to_html(full_html=False)
    tabela = gerar_tabela(dados_tratados)
    tabela_html = tabela.to_html(full_html=False)

    return jsonify({
        'grafico_barras_html': grafico_barras_html,
        'grafico_linhas_html': grafico_linhas_html,
        'tabela_html': tabela_html
    })


if __name__ == '__main__':
    app.run(debug=True)
