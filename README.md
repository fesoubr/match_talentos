# Match de Talentos: Sistema de Recomendação Inteligente para Recrutamento


##  Sobre o Projeto

O **Match de Talentos** é um sistema de recomendação inteligente desenvolvido para revolucionar o processo de recrutamento. Utilizando técnicas avançadas de **Processamento de Linguagem Natural (PLN)**, a aplicação analisa e compara descrições de vagas com perfis de candidatos para calcular um *score* de compatibilidade.

O objetivo principal é simples e poderoso: **identificar e classificar os candidatos mais qualificados para cada vaga** com base na similaridade de suas habilidades e experiências. Ao automatizar essa análise, a ferramenta permite que recrutadores foquem seu tempo e energia nos talentos com maior potencial, tornando o processo de seleção mais ágil, preciso e eficiente.

## Funcionalidades Principais

-   **Análise de Vagas e Currículos**: Processa textos não estruturados de descrições de vagas e perfis de candidatos.
-   **Cálculo de Similaridade**: Utiliza o método de **similaridade de cossenos** para quantificar a compatibilidade entre vaga e candidato.
-   **Ranking Inteligente**: Gera uma lista ordenada dos candidatos mais aderentes para uma vaga específica.
-   **Interface Web Interativa**: Uma aplicação amigável construída com Streamlit para facilitar o uso por recrutadores.

## Tecnologias Utilizadas

| Ferramenta             | Propósito                                       |
| ---------------------- | ----------------------------------------------- |
| **Python** | Linguagem principal do projeto.                 |
| **Pandas** | Análise e manipulação de dados.                 |
| **Scikit-learn** | Vetorização TF-IDF e cálculo de similaridade.   |
| **spaCy** | Pré-processamento de texto em português.        |
| **Streamlit** | Criação da interface web interativa.            |

---

## Começando

Siga os passos abaixo para configurar o ambiente e executar a aplicação localmente.

### 1. Pré-requisitos

-   [Python 3.8+](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/downloads)

### 2. Instalação

**1. Clone o repositório:**

```bash
git clone [https://github.com/fesoubr/match_talentos.git](https://github.com/fesoubr/match_talentos.git)
cd match_talentos
```

**2. Crie e ative um ambiente virtual:**

É uma boa prática usar ambientes virtuais para isolar as dependências do projeto.

-   **Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
-   **macOS / Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

**3. Instale as bibliotecas:**

Crie um arquivo `requirements.txt` na raiz do projeto com o seguinte conteúdo:

```txt
pandas
scikit-learn
streamlit
spacy
```

Em seguida, execute o comando de instalação:

```bash
pip install -r requirements.txt
```

**4. Baixe o modelo de linguagem do spaCy:**

O projeto utiliza o modelo de língua portuguesa para o processamento de texto.

```bash
python -m spacy download pt_core_news_sm
```

### 3. Rodando a Aplicação

Com tudo instalado, inicie o servidor do Streamlit.

**1. Navegue até o diretório do aplicativo:**

```bash
cd app
```

**2. Execute o Streamlit:**

```bash
streamlit run app.py
```

Pronto! A aplicação será aberta automaticamente no seu navegador. 🎉

---

## Como Treinar o Modelo com Novos Dados

O "treinamento" neste projeto consiste em processar novos dados de candidatos e gerar um novo modelo de vetorização (TF-IDF). Para isso, utilize o notebook disponibilizado.

**1. Abra o Notebook no Google Colab:**

Acesse o notebook através do link abaixo. Ele contém todo o fluxo de pré-processamento e treinamento.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1SJ-zOfiGDhmHU9HLtZQOX0_4LaiWdDYA)

**2. Prepare seus Dados:**

No ambiente do Colab, faça o upload dos seus arquivos CSV atualizados:
-   `df_cand.csv`: Tabela com os dados dos candidatos.
-   `df_vagas.csv`: Tabela com os dados das vagas.

**3. Execute Todas as Células:**

Execute o notebook do início ao fim. O código irá:
-   Limpar e processar os textos.
-   Treinar um novo `TfidfVectorizer`.
-   Gerar os arquivos de saída.

**4. Salve os Artefatos Gerados:**

Ao final da execução, o notebook irá gerar dois arquivos essenciais. Faça o download deles:
-   `vectorizer.pkl`: O modelo de vetorização TF-IDF treinado.
-   `df_cand_proc.csv`: A base de dados de candidatos com o texto já processado.

**5. Atualize a Aplicação:**

-   Copie os dois arquivos que você baixou (`vectorizer.pkl` e `df_cand_proc.csv`).
-   Cole-os dentro da pasta `app/` do seu projeto local, **substituindo os arquivos antigos**.

Após substituir os arquivos, reinicie o aplicativo Streamlit. Ele passará a usar o modelo e os dados mais recentes para as recomendações.
