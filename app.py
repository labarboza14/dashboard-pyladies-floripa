import pandas as pd
import plotly.express as px
import plotly.io as pio
from flask import Flask, render_template

app = Flask(__name__)

# Função para carregar os dados
def carregar_dados():
    df = pd.read_excel("dados.xlsx")
    df.columns = df.columns.str.strip()  # Remover espaços extras nas colunas
    return df

@app.route('/')
def index():
    df = carregar_dados()

    # Gráfico 1: Faixa etária
    fig1 = px.histogram(df, x="Qual é a sua faixa etária", color_discrete_sequence=["#1f77b4"])
    graph1 = pio.to_html(fig1, full_html=False, include_plotlyjs="cdn")

    # Gráfico 2: Conheciam a Linuxtips
    fig2 = px.histogram(df, x="Você já conhecia a Linuxtips?", color_discrete_sequence=["#e6a100"])
    graph2 = pio.to_html(fig2, full_html=False, include_plotlyjs="cdn")

    # Gráfico 3: Área de trabalho
    fig3 = px.histogram(df, x="Você trabalha em qual área?", color_discrete_sequence=["#1f77b4"])
    graph3 = pio.to_html(fig3, full_html=False, include_plotlyjs="cdn")

    # Gráfico 4: Faixa de renda
    fig4 = px.histogram(df, x="Qual é a sua faixa de renda", color_discrete_sequence=["#e6a100"])
    graph4 = pio.to_html(fig4, full_html=False, include_plotlyjs="cdn")

    # Gráfico 5: Cursos mais escolhidos
    cursos_series = df["Na primeira edição da Escola PYLADIES FLORIPA, você pode escolher até 3 cursos para realizar nos próximos 3 meses."]
    todos_os_cursos = cursos_series.dropna().str.split(",").explode().str.strip()  # Separar os cursos
    cursos_count = todos_os_cursos.value_counts().reset_index()
    cursos_count.columns = ["Curso", "Quantidade"]
    fig5 = px.bar(cursos_count, x="Curso", y="Quantidade", color_discrete_sequence=["#1f77b4"])
    graph5 = pio.to_html(fig5, full_html=False, include_plotlyjs="cdn")

    # Renderizar o template HTML com os gráficos
    return render_template('index.html', graph1=graph1, graph2=graph2, graph3=graph3, graph4=graph4, graph5=graph5)

if __name__ == '__main__':
    app.run(debug=True)
