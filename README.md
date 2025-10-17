# Análise de Falhas na Entrega de Rações

## Introdução

Este projeto realiza uma análise aprofundada das falhas na entrega de rações, com base em dados de uma pesquisa interna. O objetivo é identificar os principais problemas, compreender as suas causas e propor soluções estratégicas para otimizar o processo logístico, melhorar a satisfação dos clientes e garantir o bem-estar animal.

A análise utiliza técnicas de Processamento de Linguagem Natural (PLN) para extrair insights a partir das respostas qualitativas da pesquisa, segmentando os resultados por perfil de entrevistado (Produtor, Motorista, Gestão, etc.) e gerando visualizações de dados para facilitar a compreensão dos resultados.

## Estrutura do Projeto

O repositório está organizado da seguinte forma:

- **`assets/`**: Contém os dados brutos da pesquisa em formato `.xlsx`.
- **`docs/`**: Armazena a documentação do projeto, incluindo a análise detalhada e os resultados consolidados.
- **`notebooks/`**: Contém os notebooks Jupyter utilizados para a exploração e análise inicial dos dados.
- **`plots/`**: Guarda os gráficos gerados pela análise, como os diagramas de Pareto e os gráficos de barras.
- **`src/`**: Inclui os scripts Python responsáveis pelo processamento, análise e visualização dos dados.
  - **`process_and_segment_data.py`**: Script para processar e segmentar os dados da pesquisa por perfil.
  - **`generate_charts.py`**: Script para gerar os gráficos e visualizações.
  - **`strategic_analysis.py`**: Script para realizar a análise estratégica e priorização de problemas.
  - **`utils/`**: Módulos de utilidades, como o de logging.

## Como Executar a Análise

Para executar a análise completa e gerar os resultados, siga os passos abaixo:

1. **Instale as dependências:**

   ```bash
   pip install pandas matplotlib seaborn
   ```

2. **Execute os scripts de análise na ordem correta:**

   ```bash
   python src/process_and_segment_data.py
   python src/generate_charts.py
   python src/strategic_analysis.py
   ```

Após a execução, os resultados atualizados estarão disponíveis nos diretórios `docs/` e `plots/`.

## Principais Descobertas

A análise revelou que os problemas na entrega de rações são sistêmicos e afetam toda a cadeia produtiva. As principais categorias de falhas identificadas foram:

1.  **Gestão de Insumos e Estoque**: Problemas relacionados com a falta ou sobra de ração, e a capacidade de produção da fábrica.
2.  **Processos e Informação**: Falhas na comunicação entre os diferentes setores e a falta de automação nos processos.
3.  **Logística e Distribuição**: Atrasos na entrega, erros de tipo ou local de descarga e problemas no planejamento de rotas.

A análise de Pareto destacou que a **Gestão de Insumos e Estoque** é a categoria com maior impacto, representando a maior parte das ocorrências.

## Recomendações

Com base na análise, a principal recomendação é a **implementação de um sistema de gestão de estoque em tempo real**, que inclua sensores de nível nos silos das granjas. Esta ação permitiria um planejamento de demanda mais preciso e proativo, reduzindo significativamente os casos de falta e sobra de ração.

Outras ações estratégicas sugeridas incluem:

- **Otimizar o planejamento de rotas** através de um sistema de gestão de transportes (TMS).
- **Criar um canal de comunicação centralizado** para facilitar a interação entre produtores, motoristas e a fábrica.
- **Automatizar os processos de pedidos** para reduzir erros manuais e agilizar o fluxo de informação.

Para mais detalhes, consulte o documento de análise completa em `docs/Análise da Pesquisa sobre Falhas na Entrega de Rações.md`.
