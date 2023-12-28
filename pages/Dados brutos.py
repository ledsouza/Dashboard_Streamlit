import streamlit as st
import requests
import pandas as pd

st.title('DADOS BRUTOS')

url = 'https://labdados.com/produtos'

response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())
dados['Data da Compra'] = pd.to_datetime(dados['Data da Compra'], format = '%d/%m/%Y')

with st.expander('Colunas'):
    colunas = st.multiselect('Selecione as colunas', list(dados.columns), list(dados.columns))

st.sidebar.title('Filtros')
with st.sidebar.expander('Nome do produto'):
    produtos = st.multiselect('Selecione os produtos', dados['Produto'].unique(), dados['Produto'].unique())
with st.sidebar.expander('Categoria do produto'):
    categoria_produto = st.multiselect('Selecione a categoria', dados['Categoria do Produto'].unique(), dados['Categoria do Produto'].unique())
with st.sidebar.expander('Preço do produto'):
    preco = st.slider('Selecione o preço', 0, 5000, (0,5000))
with st.sidebar.expander('Frete da compra'):
    frete = st.slider('Selecione o frete', 0.0, dados['Frete'].max(), (0.0, dados['Frete'].max()))
with st.sidebar.expander('Data da compra'):
    data_compra = st.date_input('Selecione a data', (dados['Data da Compra'].min(), dados['Data da Compra'].max()))
with st.sidebar.expander('Vendedor'):
    vendedor = st.multiselect('Nome do vendedor', dados['Vendedor'].unique(), dados['Vendedor'].unique())
with st.sidebar.expander('Local da compra'):
    local_compra = st.multiselect('Selecione o local da compra', dados['Local da compra'].unique(), dados['Local da compra'].unique())
with st.sidebar.expander('Tipo de pagamento'):
    pagamento = st.multiselect('Selecione o tipo de pagamento', dados['Tipo de pagamento'].unique(), dados['Tipo de pagamento'].unique())
with st.sidebar.expander('Quantidade de parcelas'):
    parcelas = st.slider('Selecione a quantidade de parcelas', 1, 12, (1, 12))
with st.sidebar.expander('Avaliação da compra'):
    avaliacao = st.slider('Selecione a avaliação', dados['Avaliação da compra'].min(), dados['Avaliação da compra'].max(), (dados['Avaliação da compra'].min(), dados['Avaliação da compra'].max()))

st.dataframe(dados)