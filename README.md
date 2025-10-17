# Análise de Falhas na Entrega de Rações: Otimizando a Cadeia de Valor do Frango de Corte

## Visão Geral

Este projeto apresenta um diagnóstico estratégico e um plano de ação para resolver as falhas crônicas na cadeia de entrega de rações para a avicultura de corte. A análise utiliza dados de uma pesquisa com 68 stakeholders e aplica Processamento de Linguagem Natural (NLP) para identificar as causas raiz dos problemas e propor uma solução sistêmica, visando otimizar a eficiência operacional e os resultados zootécnicos.

---

## O Problema em Números: Diagnóstico Quantitativo

A análise dos dados revelou que o problema é sistêmico e de alta severidade, com três categorias críticas se destacando:

| Problema | Frequência | Severidade | Maior Impacto em |
| :--- | :--- | :--- | :--- |
| **Atraso ou Falta de Ração** | 40% dos relatos | Alta | Produtores |
| **Sobra de Ração** | 24% dos relatos | Média | Gestão |
| **Problemas Logísticos** | 19% dos relatos | Alta | Motoristas |

**Insights Chave:**
*   **Sistemicidade:** 74% dos respondentes relataram mais de um tipo de problema.
*   **Correlação:** Existe uma alta correlação (0,78) entre falhas de comunicação e problemas logísticos, indicando que a melhoria na comunicação é fundamental.
*   **Foco em Comunicação:** 87% das sugestões de melhoria mencionam a necessidade de aprimorar a comunicação.

### Impactos Quantificados na Cadeia de Valor

| Tipo de Impacto | Dado Quantificado |
| :--- | :--- |
| **Desempenho Zootécnico** | 82% dos produtores relataram queda no ganho de peso das aves. |
| **Conversão Alimentar (CA)** | 65% relataram piora na conversão alimentar. |
| **Impacto Econômico** | Estimativa de perda de **3 a 5%** na conversão alimentar por lote. |
| **Prejuízos Financeiros** | 74% dos respondentes citaram prejuízos financeiros diretos. |
| **Custo Operacional** | 58% relataram custos adicionais com replanejamento e alocação de recursos. |

---

## A Solução: Uma Abordagem Sistêmica em Três Pilares

A solução proposta é baseada em uma abordagem integrada para atacar as causas raiz dos problemas.

### 1. Comunicação Eficiente
*   **Ação:** Implementar um **canal centralizado** (aplicativo ou portal) para gestão de pedidos, acompanhamento de status em tempo real e comunicação de ocorrências.
*   **Alinhamento Interno:** Melhorar a integração e a comunicação entre as equipes de PCP, expedição e logística.

### 2. Processos Otimizados
*   **Ação:** Mapear e redesenhar o fluxo de trabalho, desde a solicitação do pedido até a entrega, para eliminar gargalos.
*   **Gestão de Sobras:** Implementar um sistema de **"Pedidos Programados com Confirmação"**, onde o produtor valida ou ajusta a entrega antes do envio, reduzindo o desperdício.

### 3. Tecnologia Habilitadora
*   **Logística:** Adotar um **Sistema de Gestão de Entregas (TMS)** para otimizar rotas, sequenciar entregas e rastrear os veículos em tempo real.
*   **Estoque:** Instalar **sensores de nível (IoT) nos silos** das granjas para monitoramento remoto do estoque, permitindo um planejamento de produção proativo.
*   **Planejamento:** Utilizar **análise de dados e modelos de previsão** para otimizar a produção e o roteamento.

---

## Roadmap de Implementação (12 Meses)

| Fase | Período | Foco | Meta Principal |
| :--- | :--- | :--- | :--- |
| **1: Diagnóstico e Planejamento** | Nov/Dez 2025 | Mapeamento de processos e definição de KPIs. | Redução de 15% nas falhas em 6 meses. |
| **2: Implementação Tecnológica** | Jan/Mar 2026 | Implantação da plataforma e dos sensores de nível piloto. | 100% dos pedidos via sistema até o final do 1º trimestre. |
| **3: Otimização Logística** | Abr/Jun 2026 | Implementação do TMS e revisão dos processos. | Redução de 20% no tempo médio de entrega. |
| **4: Expansão e Consolidação** | Jul/Dez 2026 | Expansão das soluções para 100% das granjas. | Redução de 80% nas falhas de entrega até o final de 2026. |

---

## Sobre Este Repositório

Este repositório contém o código-fonte e os artefatos da análise de dados descrita. O objetivo é fornecer uma base reproduzível para a exploração dos dados e validação dos insights.

### Como Executar a Análise

A análise pode ser executada de duas maneiras:

1.  **Via Script Principal:**
    O `main.py` orquestra todo o pipeline: processa os dados, gera as análises e salva os gráficos na pasta `plots/`.
    ```bash
    python main.py
    ```

2.  **Via Jupyter Notebook:**
    Para uma análise interativa e passo a passo, utilize o notebook `notebooks/analise_pesquisa_fab_racao.ipynb`.
    ```bash
    jupyter notebook notebooks/analise_pesquisa_fab_racao.ipynb
    ```

### Requisitos e Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/brunocorisco86/mealfactorynlpanalysis.git
    cd mealfactorynlpanalysis
    ```

2.  **Crie um ambiente virtual e instale as dependências:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

### Estrutura de Pastas

```
/
├── assets/              # Arquivos de dados brutos (ex: .xlsx)
├── docs/                # Documentos de análise gerados
├── knowledge/           # Materiais de referência
├── notebooks/           # Jupyter Notebooks da análise
├── plots/               # Gráficos e imagens gerados
├── presentation/        # Apresentações do projeto
├── src/                 # Código-fonte modularizado
├── .gitignore
├── main.py              # Script principal para orquestrar a análise
├── README.md            # Este arquivo
└── requirements.txt     # Dependências do projeto
```

### Próximos Passos

*   **Validação Aprofundada:** Realizar workshops com os stakeholders para refinar o diagnóstico.
*   **Desenvolvimento de Protótipos:** Criar e testar protótipos das soluções (App, Sensores, TMS) em um projeto piloto com 5-10 granjas.
*   **Dashboard de Monitoramento:** Construir um dashboard com os KPIs de entrega para acompanhamento em tempo real por todos os envolvidos.
