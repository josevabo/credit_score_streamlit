# Análise de Crédito com Streamlit

## Objetivo

Este projeto tem como objetivo disponibilizar uma aplicação para avaliação de crédito, através de machine learning, a partir da informação de dados pessoais do usuário.

A interface foi possível com o uso do streamlit. O streamlit permite subir um servidor de aplicação python local, com uma interface amigável.

Neste projeto a aplicação disponibilizada recebe os dados pessoais preenchidos e as passa por um modelo de Machine Learning que responderá se o crédito pode ser aprovado ou não diante dos resultados obtidos no seu treino.

## Instalação

Para instalação do projeto, inicialmente instalar as dependências do projeto:
> ` pip install -r requirements.txt `

Junto das dependências será instalado também o pacote `streamlit`. Para execução da aplicação localmente, executar o comando via streamlit:
> `streamlit run simulador.py`

A aplicação também está publicada em página do streamlit:

<https://share.streamlit.io/josevabo/credit_score_streamlit/main/simulador.py>

## Machine Learning

O modelo foi treinado a partir de uma base de dados fictícia contendo, inicialmente, mais de um milhão de registros.

Todo o processo de análise e tratamento dos dados, até o treino do modelo utilizado na aplicação está disponível no diretório "/notebook" deste projeto.
