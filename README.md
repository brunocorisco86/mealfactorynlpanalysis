# Análise de Falhas na Entrega de Rações: Otimizando a Cadeia de Valor do Frango de Corte

Este documento apresenta o diagnóstico estratégico e as recomendações para melhoria operacional da cadeia de entrega de rações, visando otimizar a Cadeia de Valor do Frango de Corte. O projeto utiliza técnicas de Processamento de Linguagem Natural (NLP) para analisar dados de uma pesquisa qualitativa, extrair insights, identificar as causas raiz dos problemas e sugerir ações para a melhoria dos processos.

---

## O Problema Central

Falhas crônicas na entrega de rações afetam toda a cadeia produtiva do frango de corte. Os problemas principais incluem:
*   Atrasos na entrega, causando jejum das aves.
*   Volumes incorretos, gerando desperdício.
*   Erros no tipo de ração fornecida.
*   Comunicação falha entre os stakeholders.

## Metodologia de Análise

O diagnóstico foi baseado em uma pesquisa qualitativa com múltiplos atores da cadeia para compreender profundamente os problemas.

*   **Perfis Analisados:** Produtores, Veterinários/Extensionistas, Motoristas, e Gestão (Fábrica, PCP, Expedição).
*   **Objetivo:** Mapear as causas raiz dos problemas e propor ações estratégicas.

---

## Resultados: Perspectivas dos Atores

A pesquisa revelou que as falhas são um problema crônico que afeta todos os envolvidos, gerando frustração, preocupação e pressão.

### Produtores (Sentimento: Frustração e Impotência)
*   **Problemas:** Atrasos (jejum das aves), volumes maiores que o solicitado (sobra), erro no tipo de ração, e falta de informações precisas.
*   **Impactos:** Prejuízos zootécnicos (redução no ganho de peso, piora na conversão alimentar) e problemas sanitários (aumento de dermatose e problemas intestinais).
*   **Expectativa:** Entregas pontuais e confiáveis, volumes exatos e comunicação clara.

### Veterinários/Extensionistas (Sentimento: Preocupação Técnica)
*   **Problemas:** Falhas logísticas interferem no planejamento alimentar e sanitário, e atuam como intermediários na resolução de problemas, gerando desgaste.
*   **Sugestões:** Implementar um sistema de rastreamento de pedidos e melhorar a comunicação entre fábrica, logística e campo.

### Motoristas (Sentimento: Pressão e Sobrecarga)
*   **Problemas:** Rotas mal otimizadas, jornadas de trabalho extensas e comunicação inadequada sobre locais e condições de acesso.
*   **Sugestões:** Implementar um sistema de planejamento de rotas mais eficiente e melhorar a comunicação com a expedição e os produtores.

### Gestão (Sentimento: Consciência dos Desafios Operacionais)
*   **Problemas:** Falta de visibilidade do estoque em campo, dependência de processos manuais e capacidade limitada de produção e armazenamento.
*   **Sugestões:** Automação de processos e implementação de um sistema de gestão de estoque com visibilidade em tempo real.

---

## A Solução: Abordagem Sistêmica em Três Pilares

A solução exige uma abordagem integrada e sistêmica que envolve três pilares fundamentais: Comunicação Eficiente, Processos Otimizados e Tecnologia Habilitadora.

### 1. Comunicação Eficiente
*   **Ação:** Implementar um canal centralizado (aplicativo ou portal online) para pedidos e acompanhamento de status em tempo real.
*   **Interna:** Melhorar a comunicação e o alinhamento entre PCP, expedição e logística.

### 2. Processos Otimizados
*   **Ação:** Mapear e redesenhar o fluxo de entrega para eliminar gargalos.
*   **Foco na Sobra:** Implementar um sistema de "Pedidos Programados com Confirmação" para evitar o envio de ração desnecessária.

### 3. Tecnologia Habilitadora
*   **Logística:** Adotar um Sistema de Gestão de Entregas (TMS) para otimizar rotas e rastrear os caminhões.
*   **Estoque:** Instalar sensores de nível nos silos das granjas para visibilidade do estoque em tempo real.
*   **Planejamento:** Utilizar análise de dados e modelos de previsão para otimizar a produção.

---

## Benefícios Esperados

| Para a Empresa | Para os Produtores | Para os Animais |
| :--- | :--- | :--- |
| Aumento de Produtividade | Confiabilidade (entregas pontuais) | Bem-estar Animal (nutrição sem jejum) |
| Redução de Custos | Rentabilidade (melhor desempenho zootécnico) | Saúde Melhorada (redução de problemas sanitários) |
| Melhoria de Imagem e Competitividade | Redução de Estresse | Desempenho Zootécnico Otimizado |

---

## Sobre este Repositório

Este repositório contém todo o código e os artefatos utilizados para realizar a análise descrita acima.

### Como Executar a Análise

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

### Requisitos e Instalação

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

### Estrutura de Pastas

```
/
├── assets/              # Arquivos de dados brutos (ex: .xlsx da pesquisa)
├── docs/                # Documentos de análise gerados (ex: .txt, .md)
├── knowledge/           # Materiais de referência e conhecimento
├── notebooks/           # Jupyter Notebooks com a análise exploratória e principal
├── plots/               # Gráficos e imagens gerados pela análise
├── presentation/        # Apresentação do projeto
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

### Próximos Passos

- **Dashboard Interativo**: Desenvolver um dashboard com Streamlit ou Dash para permitir que usuários não técnicos explorem os resultados da pesquisa de forma interativa.
- **Automação do Pipeline**: Criar um pipeline automatizado (ex: com Airflow ou GitHub Actions) que execute a análise periodicamente à medida que novos dados da pesquisa são adicionados.
- **API de Classificação**: Expor o modelo de clusterização ou sentimento treinado através de uma API REST para classificar novas respostas em tempo real.
- **Aprimoramento dos Modelos**: Experimentar com modelos de linguagem mais avançados ou realizar fine-tuning específico com dados da empresa para melhorar ainda mais a precisão da classificação e clusterização.
- **Integração com Banco de Dados**: Migrar o armazenamento de dados de arquivos Excel para um banco de dados (como PostgreSQL ou SQLite) para melhor escalabilidade e gerenciamento.