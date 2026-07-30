import streamlit as st

#imprimindo uma mensagem na tela
st.write('Vamos aprender streamlit juntos')

#usando várias formatações de texto
st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

#criando elementos gráficos
'''Informar como colher os dados através de variáveis'''
x = st.checkbox('Sim')
st.title(x)
st.button('Clique')
st.radio('Selecione seu gênero',['Masculino','Feminino'])
st.selectbox('Selecione seu gênero',['Masculino','Feminino'])
st.multiselect('Escolha um departamento',['DCS', 'DE', 'DIR'])
st.select_slider('Selecione uma resposta', ['Ruim', 'Bom', 'Excelente'])
st.slider('Selecione um número', 0,50)
st.number_input('Selecione um número', 0,10)
st.text_input('Endereço de e-mail')
st.date_input('Data de viagem')
st.time_input('Tempo de escola')
st.text_area('Descrição')
st.file_uploader('Atualize uma foto')
st.color_picker('Escolha sua cor favorita')

#mensagens de status
st.success("Você conseguiu!")
st.error("Erro!")
st.warning("Advertência")
st.info("Esta é uma informação")

#criando uma aplicação simples
import streamlit as st
#import no requirements.txt
import pandas as pd

df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]
})
#posso trocar estes dados por dados de tabelas reais!

st.write("Criando uma tabela!")
#tabelas interativas
st.write(df)
#inserindo um selectbox
opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['nomeServidor'])
#O formato de print é diferente de outras versões
#de Python
st.write('Você selecionou: ', opcao)
#como filtrar os dados pelo nome?

#filtrando os dados pelo nome
dadosFiltrados = df[df['nomeServidor'] == opcao]
dadosFiltrados

import streamlit as st
import pandas as pd
#import no requirements.txt

st.title('Localização das comunidades quilombolas (2022)')

#preparando o dataframe
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#apresentar o dataframe
#https://www.ibge.gov.br/geociencias/organizacao-do-territorio/estrutura-territorial/27385-localidades.html?=&t=downloads
#apresentar o dicionario de dados (disponível em Localizado em "Downloads > Localidades quilombolas > Arquivos vetoriais > dicionario LQs")
#informar que dados são remanunfaturados (vamos aproveitar dados de pesquisas já em andamento)

#informar que precisa limpar os dados
df.info()

#criando um slider
numero = st.slider('Selecione um número de linhas a serem exibidas', min_value = 0, max_value = 100)
st.write(df.head(numero))

#visualizando o número de comunidades por estado
df['NM_UF'].value_counts()

#criando um gráfico de barras
st.bar_chart(df['NM_UF'].value_counts())

import os
import pandas as pd
import matplotlib.pyplot as plt

# Caminho exato do arquivo no Google Colab
caminho_arquivo = "/content/drive/MyDrive/bcdata.sgs.25388.csv"

print("Verificando arquivo e carregando dados...")

if not os.path.exists(caminho_arquivo):
    print(f"\n O arquivo '{caminho_arquivo}' não foi encontrado!")
else:
    try:
        # Importação configurando o padrão decimal e separador do Banco Central
        df = pd.read_csv(caminho_arquivo, sep=';', decimal=',')

        # Ajustar colunas para minúsculo e tratar formato de Data
        df.columns = [col.lower().strip() for col in df.columns]
        df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
        df['ano'] = df['data'].dt.year

        print("[SUCESSO] Dados carregados. Iniciando geração das imagens...\n")

        # -----------------------------------------------------------------
        # 1. GRÁFICO DE LINHA
        # -----------------------------------------------------------------
        plt.figure(figsize=(10, 5))
        plt.plot(df['data'], df['valor'], color='#1f77b4', linewidth=2)
        plt.title('Evolução Temporal do IBCR-NE', fontsize=12, fontweight='bold', pad=15)
        plt.xlabel('Anos da Série Histórica', fontsize=10)
        plt.ylabel('Valor do Indicador', fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()

        # Salva o gráfico 1 na pasta
        plt.savefig('grafico_linha.png', dpi=300)
        plt.show()

        # ------------------------------------------------
        # 2. GRÁFICO DE BARRAS
        # ------------------------------------------------
        media_anual = df.groupby('ano')['valor'].mean().reset_index()

        plt.figure(figsize=(12, 5))
        plt.bar(media_anual['ano'], media_anual['valor'], color='teal', edgecolor='black', alpha=0.8)
        plt.title('Comparativo de Média Anual do Indicador', fontsize=12, fontweight='bold', pad=15)
        plt.xlabel('Ano Correspondente', fontsize=10)
        plt.ylabel('Valor Médio Registrado', fontsize=10)
        plt.xticks(media_anual['ano'], rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()

        # Salva o gráfico 2 na pasta
        plt.savefig('grafico_barras.png', dpi=300)
        plt.show()

        # -----------------------------------------------------------------
        # 3. GRÁFICO DE PIZZA
        # -----------------------------------------------------------------

        v_min, v_max = df['valor'].min(), df['valor'].max()
        intervalo = (v_max - v_min) / 3

        limite_baixo = v_min + intervalo
        limite_medio = v_min + (2 * intervalo)

        def classificar_faixa(val):
            if val <= limite_baixo:
                return 'Faixa Baixa'
            elif val <= limite_medio:
                return 'Faixa Média'
            else:
                return 'Faixa Alta'

        df['categoria'] = df['valor'].apply(classificar_faixa)
        contagem_categorias = df['categoria'].value_counts()

        # Desenhar o gráfico de pizza
        plt.figure(figsize=(8, 6))
        cores = ['#66b3ff', '#99ff99', '#ff9999']

        plt.pie(contagem_categorias,
                labels=contagem_categorias.index,
                autopct='%1.1f%%',
                startangle=140,
                colors=cores,
                wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'antialiased': True})
