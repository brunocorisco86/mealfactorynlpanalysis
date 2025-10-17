
import pandas as pd
import re

def parse_analysis_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    profiles_data = {}

    profile_sections = re.split(r'### Perfil: (.*)\n', content)[1:]
    for i in range(0, len(profile_sections), 2):
        profile_name = profile_sections[i].strip()
        profile_content = profile_sections[i+1]
        profiles_data[profile_name] = {}

        question_sections = re.split(r'#### Pergunta: (.*)\n', profile_content)[1:]
        for j in range(0, len(question_sections), 2):
            question_text = question_sections[j].strip()
            responses_content = question_sections[j+1]
            profiles_data[profile_name][question_text] = []

            responses = re.findall(r'- Resposta \d+: (.*)', responses_content)
            profiles_data[profile_name][question_text].extend([r.strip() for r in responses])

    return profiles_data

if __name__ == '__main__':
    analysis_file = 'analysis_by_profile.txt'
    profiles_data = parse_analysis_file(analysis_file)

    problem_themes = {
        'Falta de ração': ['falta de ração', 'sem ração', 'jejum'],
        'Sobra de ração': ['sobra de ração', 'excesso de ração', 'volume maior'],
        'Erro de entrega (tipo/local)': ['ração errada', 'tipo incorreto', 'descarga errada'],
        'Atraso na entrega': ['atraso', 'demora na entrega'],
        'Comunicação': ['comunicação', 'falha na comunicação', 'dificuldade de contato'],
        'Logística/Planejamento': ['logística', 'planejamento', 'rota', 'otimização'],
        'Sistema/Automação': ['sistema', 'automação', 'manual'],
        'Capacidade da fábrica': ['capacidade', 'produção', 'estrutura']
    }

    problem_counts_by_profile = {profile: {theme: 0 for theme in problem_themes.keys()} for profile in profiles_data.keys()}
    for profile, questions in profiles_data.items():
        for question, responses in questions.items():
            for response in responses:
                for theme, keywords in problem_themes.items():
                    for keyword in keywords:
                        if re.search(r'\b' + re.escape(keyword) + r'\b', response, re.IGNORECASE):
                            problem_counts_by_profile[profile][theme] += 1
                            break

    # Aggregate problem counts across all profiles to get total problem counts
    total_problem_counts = {theme: 0 for theme in problem_themes.keys()}
    for profile_data in problem_counts_by_profile.values():
        for theme, count in profile_data.items():
            total_problem_counts[theme] += count

    # Define problem categories
    categories = {
        'Gestão de Insumos e Estoque': ['Falta de ração', 'Sobra de ração', 'Capacidade da fábrica'],
        'Logística e Distribuição': ['Logística/Planejamento', 'Atraso na entrega', 'Erro de entrega (tipo/local)'],
        'Processos e Informação': ['Comunicação', 'Sistema/Automação']
    }

    category_counts = {cat: 0 for cat in categories.keys()}

    for category, problems_in_category in categories.items():
        for problem_theme_key in problems_in_category:
            if problem_theme_key in total_problem_counts:
                category_counts[category] += total_problem_counts[problem_theme_key]

    df_categories = pd.DataFrame(list(category_counts.items()), columns=['Categoria', 'Frequência'])
    df_categories = df_categories.sort_values(by='Frequência', ascending=False).reset_index(drop=True)
    df_categories['Frequência Cumulativa'] = df_categories['Frequência'].cumsum()
    df_categories['Porcentagem Cumulativa'] = 100 * df_categories['Frequência Cumulativa'] / df_categories['Frequência'].sum()

    # Find the category with the highest impact (80/20 rule)
    highest_impact_category = df_categories.iloc[0]

    # Output for analysis
    with open('strategic_analysis_output.txt', 'w', encoding='utf-8') as f:
        f.write('## Análise Estratégica das Categorias de Problemas\n\n')
        f.write('### Distribuição de Frequência por Categoria\n')
        f.write(df_categories.to_markdown(index=False))
        f.write('\n\n### Priorização por Impacto (Regra 80/20)\n')
        f.write(f'A categoria de maior impacto, concentrando a maior frequência de problemas, é: **{highest_impact_category["Categoria"]}** com {highest_impact_category["Frequência"]} ocorrências, representando {highest_impact_category["Porcentagem Cumulativa"]:.2f}% do total acumulado.\n\n')

        f.write('### Hipótese de Causa Raiz para a Categoria de Maior Impacto\n')
        if highest_impact_category['Categoria'] == 'Gestão de Insumos e Estoque':
            f.write('**Causa Raiz Sugerida:** Falta de visibilidade e controle sobre o estoque em tempo real e falhas no planejamento da demanda. A ausência de um sistema integrado que monitore o consumo e o estoque nas granjas leva a decisões reativas e imprecisas, resultando em falta ou sobra de ração.\n\n')
        elif highest_impact_category['Categoria'] == 'Logística e Distribuição':
            f.write('**Causa Raiz Sugerida:** Ineficiência no planejamento de rotas e na coordenação de entregas. A falta de otimização e a comunicação deficiente entre expedição e motoristas contribuem para atrasos e erros, impactando a eficiência operacional.\n\n')
        elif highest_impact_category['Categoria'] == 'Processos e Informação':
            f.write('**Causa Raiz Sugerida:** Processos manuais e comunicação fragmentada. A dependência de métodos não automatizados e a falta de um fluxo de informação claro entre as áreas geram gargalos, retrabalho e erros na gestão da entrega.\n\n')

        f.write('### Ação Estratégica Sugerida\n')
        if highest_impact_category['Categoria'] == 'Gestão de Insumos e Estoque':
            f.write('**Iniciativa Prioritária:** Implementação de um sistema de gestão de estoque em tempo real e otimização do planejamento de demanda. Isso incluiria a instalação de sensores de nível nos silos das granjas e a integração com um software que permita prever o consumo e gerenciar os pedidos de forma proativa.\n\n')
        elif highest_impact_category['Categoria'] == 'Logística e Distribuição':
            f.write('**Iniciativa Prioritária:** Desenvolvimento e implementação de um sistema de otimização de rotas e monitoramento de frotas. Isso permitiria planejar as entregas de forma mais eficiente, reduzir atrasos, minimizar erros e melhorar a comunicação com os motoristas e produtores.\n\n')
        elif highest_impact_category['Categoria'] == 'Processos e Informação':
            f.write('**Iniciativa Prioritária:** Automação e integração dos processos de comunicação e gestão de pedidos. A criação de uma plataforma unificada para solicitação, acompanhamento e comunicação de problemas eliminaria a dependência de métodos manuais e melhoraria a fluidez da informação entre todos os envolvidos.\n\n')

    print('Análise estratégica salva em strategic_analysis_output.txt')

