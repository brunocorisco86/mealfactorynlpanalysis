# Análise de Pesquisa sobre Falhas na Entrega de Rações

Este projeto realiza uma análise aprofundada de dados de uma pesquisa qualitativa sobre as falhas percebidas no processo de entrega de rações. Utilizando técnicas de Processamento de Linguagem Natural (NLP), o objetivo é extrair insights valiosos, identificar as principais causas dos problemas e sugerir ações estratégicas para a melhoria dos processos.

## Features

- **Processamento e Segmentação de Dados**: Carrega os dados da pesquisa a partir de um arquivo Excel, realiza a limpeza e segmenta as respostas por perfil de respondente.
- **Análise de Frequência e Pareto**: Identifica e quantifica os principais problemas e sugestões, gerando gráficos de Pareto para priorizar as causas mais impactantes.
- **Análise de Tópicos com LDA**: Utiliza a modelagem de tópicos (Latent Dirichlet Allocation) para uma primeira identificação dos temas gerais mencionados nas respostas.
- **Análise de Sentimento com Transformers**: Aplica um modelo de linguagem pré-treinado (`DistilBERT`) para classificar o sentimento de cada resposta (positivo, negativo ou neutro), compreendendo a percepção geral dos participantes.
- **Clusterização Semântica**: Emprega `Sentence Transformers` para converter as respostas em vetores semânticos (embeddings) e os agrupa por similaridade, permitindo a descoberta de clusters de problemas e sugestões com alta coesão contextual.
- **Visualização de Dados**: Gera e exibe múltiplos gráficos e visualizações, incluindo nuvens de palavras, gráficos de barras, diagramas de Pareto e visualizações t-SNE dos clusters semânticos.
- **Notebook Interativo**: Centraliza toda a análise em um Jupyter Notebook (`analise_pesquisa_fab_racao.ipynb`), permitindo a execução passo a passo e a exploração dos resultados.

## Estrutura de Pastas

```
/
├── assets/              # Arquivos de dados brutos (ex: .xlsx da pesquisa)
├── docs/                # Documentos de análise gerados (ex: .txt, .md)
├── knowledge/           # Materiais de referência e conhecimento
├── notebooks/           # Jupyter Notebooks com a análise exploratória e principal
├── plots/               # Gráficos e imagens gerados pela análise
├── src/                 # Código-fonte modularizado
│   ├── utils/           # Módulos de utilidade (ex: logger)
│   ├── generate_charts.py
│   ├── process_and_segment_data.py
│   └── strategic_analysis.py
├── .gitignore
├── main.py              # Script principal para orquestrar a execução da análise
├── README.md            # Este arquivo
└── requirements.txt     # Dependências do projeto
```

## Requisitos e Instalação

Para executar este projeto, você precisará do Python 3.8+ e das dependências listadas no arquivo `requirements.txt`.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/brunocorisco86/mealfactorynlpanalysis.git
    cd mealfactorynlpanalysis
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## Como Executar

A análise completa pode ser executada de duas maneiras:

1.  **Via script principal:**
    Execute o `main.py` na raiz do projeto. Ele irá processar os dados, gerar as análises e salvar os gráficos na pasta `plots/`.
    ```bash
    python main.py
    ```

2.  **Via Jupyter Notebook:**
    Para uma análise interativa e visualização detalhada, abra e execute as células do notebook `notebooks/analise_pesquisa_fab_racao.ipynb`.
    ```bash
    jupyter notebook notebooks/analise_pesquisa_fab_racao.ipynb
    ```

## Possíveis Próximos Passos (Next Steps)

- **Dashboard Interativo**: Desenvolver um dashboard com Streamlit ou Dash para permitir que usuários não técnicos explorem os resultados da pesquisa de forma interativa.
- **Automação do Pipeline**: Criar um pipeline automatizado (ex: com Airflow ou GitHub Actions) que execute a análise periodicamente à medida que novos dados da pesquisa são adicionados.
- **API de Classificação**: Expor o modelo de clusterização ou sentimento treinado através de uma API REST para classificar novas respostas em tempo real.
- **Aprimoramento dos Modelos**: Experimentar com modelos de linguagem mais avançados ou realizar fine-tuning específico com dados da empresa para melhorar ainda mais a precisão da classificação e clusterização.
- **Integração com Banco de Dados**: Migrar o armazenamento de dados de arquivos Excel para um banco de dados (como PostgreSQL ou SQLite) para melhor escalabilidade e gerenciamento.