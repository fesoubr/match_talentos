import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# --- Configuração da Página ---
st.set_page_config(
    page_title="Match de Talentos | Decision",
    page_icon="🎯",
    layout="wide"
)

# --- Funções de Carregamento ---
@st.cache_data
def carregar_artefatos():
    df_completo = pd.read_pickle('../models/df_final.pkl')
    df_candidatos = pd.read_pickle('../models/df_candidatos.pkl')
    with open('../models/vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('../models/matriz_cvs.pkl', 'rb') as f:
        matriz_cvs = pickle.load(f)
    return df_completo, df_candidatos, vectorizer, matriz_cvs

# --- Título e Descrição ---
st.title('🎯 Plataforma de Match de Talentos')
st.markdown("""
Esta ferramenta ajuda os recrutadores da **Decision** a encontrar os melhores talentos de forma rápida e precisa, utilizando Inteligência Artificial para ranquear os candidatos mais compatíveis com cada vaga.
""")

# --- Carregando os dados e modelos ---
df_final, df_candidatos, tfidf_vectorizer, matriz_tfidf_cvs = carregar_artefatos()

# --- Lógica da Barra Lateral Simplificada ---
st.sidebar.header('Selecione a Vaga')

# Mantemos a lógica para filtrar apenas as vagas que podem ser consideradas "abertas"
vagas_com_contratados = df_final[df_final['situacao_candidado'].str.contains("Contratado", na=False)]['id_vaga'].unique()
titulos_vagas_abertas = df_final[~df_final['id_vaga'].isin(vagas_com_contratados)]['titulo_vaga'].unique()

# O selectbox agora usa diretamente a lista de vagas abertas, sem o campo de pesquisa
vaga_selecionada = st.sidebar.selectbox(
    'Escolha uma vaga para ver os melhores candidatos:',
    titulos_vagas_abertas
)

# --- Lógica de Exibição do Ranking (não muda) ---
if vaga_selecionada:
    st.header(f"Buscando em toda a base os melhores candidatos para: {vaga_selecionada}")

    # 1. Encontra o texto completo da vaga selecionada
    texto_vaga = df_final[df_final['titulo_vaga'] == vaga_selecionada]['texto_vaga_completo'].iloc[0]

    # 2. Transforma o texto dessa vaga em um vetor TF-IDF
    vetor_vaga = tfidf_vectorizer.transform([texto_vaga])

    # 3. Calcula a similaridade do vetor da vaga contra a matriz de TODOS os CVs
    scores = cosine_similarity(vetor_vaga, matriz_tfidf_cvs)

    # 4. Adiciona os scores ao DataFrame de candidatos
    df_candidatos['match_score'] = scores[0]

    # 5. Ordena os candidatos pela nova pontuação de match
    df_ranking = df_candidatos.sort_values(by='match_score', ascending=False)
    
    # 6. Prepara para exibição
    df_ranking_display = df_ranking.rename(columns={
        'nome_x': 'Candidato(a)',
        'match_score': 'Pontuação de Match',
        'nivel profissional': 'Nível do Candidato',
        'situacao_candidado': 'Status Conhecido'
    })
    
    df_ranking_display['Pontuação de Match'] = df_ranking_display['Pontuação de Match'].apply(lambda x: f"{x:.2%}")

    # 7. Define as colunas a serem exibidas e mostra a tabela
    colunas_para_exibir = ['Candidato(a)', 'Pontuação de Match', 'Nível do Candidato', 'Status Conhecido']
    st.table(df_ranking_display[colunas_para_exibir].head(10).reset_index(drop=True))