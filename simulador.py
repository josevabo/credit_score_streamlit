import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from utils import Transformador
from joblib import load

def avaliar_credito(dict_features):
    modelo = load('objetos/modelo.joblib')
    features = load('objetos/features.joblib')

    if sorted(list(dict_features.keys())) == sorted(features.to_list()):
        df = pd.DataFrame(dict_features, index=[0])
        mau = modelo.predict(df)

        return mau
    else:
        st.error("Faltam dados para avaliação. Por favor, preencha todos os campos.")

st.write('''
    <style>
        li[role="option"]:hover {
            background-color:rgb(68 99 137);
        }

        [data-baseweb="select"]>div {
            cursor: pointer;
        }
    </style>
''', unsafe_allow_html=True)
st.image("img/bytebank_logo.png")
st.write("# Simulador de avaliação de crédito")

my_expander1 = st.beta_expander("Trabalho")
my_expander2 = st.beta_expander("Pessoal")
my_expander3 = st.beta_expander("Família")

lista_campos = load("objetos/lista_campos.joblib")
dict_respostas = {}

with my_expander1:
    col1, col2 = st.beta_columns(2)

    dict_respostas['Categoria_de_renda'] = col1.selectbox('Qual a categoria de renda?', lista_campos['Categoria_de_renda'])
    dict_respostas['Rendimento_Anual'] = col1.slider('Quanto é sua renda mensal?', min_value=0, max_value=35000, step=500) * 12
    dict_respostas['Tem_telefone_trabalho'] = 1 if col2.selectbox('Tem telefone no trabalho?', ['Sim','Não']) == 'Sim' else 0
    dict_respostas['Ocupacao'] = col2.selectbox('Qual sua ocupação?', lista_campos['Ocupacao'])
    is_empregado = col1.selectbox('Está empregado?', ['Sim','Não'])
    if(is_empregado == "Não"):
        dict_respostas['Anos_empregado'] = col2.slider('Há quantos anos está desempregado?', min_value=0, max_value=60) * -1
    else:
        dict_respostas['Anos_empregado'] = col2.slider('Há quantos anos está empregado?', min_value=0, max_value=60)

with my_expander2:
    col1, col2 = st.beta_columns(2)  

    dict_respostas['Idade'] = col2.slider('Qual sua idade?', min_value=18, max_value=99)
    dict_respostas['Grau_Escolaridade'] = col1.selectbox('Qual seu grau de escolaridade?', lista_campos['Grau_Escolaridade'])
    dict_respostas['Estado_Civil'] = col1.selectbox('Qual seu estado civil atualmente?', lista_campos['Estado_Civil'])
    dict_respostas['Tem_Casa_Propria'] = 1 if col2.selectbox('Tem casa própria', ['Sim','Não']) == 'Sim' else 0
    dict_respostas['Moradia'] = col1.selectbox('Como classifica seu tipo de moradia atualmente?', lista_campos['Moradia'])
    dict_respostas['Tem_telefone_fixo'] = 1 if col2.selectbox('Tem telefone em casa?', ['Sim','Não']) =='Sim' else 0
    dict_respostas['Tem_email'] =  1 if col2.selectbox('Tem e-mail?', ['Sim','Não']) =='Sim' else 0
    dict_respostas['Tem_Carro'] =  1 if col1.selectbox('Tem carro?', ['Sim','Não']) =='Sim' else 0

with my_expander3:
    col1, col2 = st.beta_columns(2) 

    dict_respostas['Tamanho_Familia'] = col1.slider('Contando com você, quantas pessoas compõem sua família?', min_value=1, max_value=20)
    dict_respostas['Qtd_Filhos'] = col2.slider('Quantos filhos você tem?', min_value=0, max_value=10)

if st.button('Enviar dados'):
    if avaliar_credito(dict_respostas):
        st.error("Infelizmente seu crédito não foi aprovado :(")
    else:
        st.success("Crédito aprovado!")

    st.write("Dados utilizados para avaliação:")
    st.write(dict_respostas)
