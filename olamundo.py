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
