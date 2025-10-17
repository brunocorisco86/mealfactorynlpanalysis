
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

def parse_analysis_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    profiles_data = {}
    current_profile = None
    current_question = None

    # Split content by profile
    profile_sections = re.split(r'### Perfil: (.*)\n', content)[1:]
    for i in range(0, len(profile_sections), 2):
        profile_name = profile_sections[i].strip()
        profile_content = profile_sections[i+1]
        profiles_data[profile_name] = {}
        current_profile = profile_name

        # Split profile content by question
        question_sections = re.split(r'#### Pergunta: (.*)\n', profile_content)[1:]
        for j in range(0, len(question_sections), 2):
            question_text = question_sections[j].strip()
            responses_content = question_sections[j+1]
            profiles_data[current_profile][question_text] = []

            # Extract responses
            responses = re.findall(r'- Resposta \d+: (.*)', responses_content)
            profiles_data[current_profile][question_text].extend([r.strip() for r in responses])

    return profiles_data

def generate_bar_chart(data, title, filename):
    df = pd.DataFrame(data).T
    df.plot(kind='bar', figsize=(12, 7))
    plt.title(title)
    plt.ylabel('Frequência')
    plt.xlabel('Perfil do Ator')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def generate_pareto_chart(data, title, filename, x_label='Categorias'):
    # Convert dictionary to DataFrame for easier manipulation
    if isinstance(data, dict):
        df_pareto = pd.DataFrame(list(data.items()), columns=[x_label, 'Frequência'])
    else:
        df_pareto = data.copy()

    df_pareto = df_pareto.sort_values(by='Frequência', ascending=False)
    
    df_pareto['Frequência Cumulativa'] = df_pareto['Frequência'].cumsum()
    df_pareto['Porcentagem Cumulativa'] = 100 * df_pareto['Frequência Cumulativa'] / df_pareto['Frequência'].sum()

    fig, ax1 = plt.subplots(figsize=(14, 8))

    # Bar chart for frequency
    ax1.bar(df_pareto[x_label], df_pareto['Frequência'], color='skyblue')
    ax1.set_xlabel(x_label)
    ax1.set_ylabel('Frequência', color='skyblue')
    ax1.tick_params(axis='y', labelcolor='skyblue')
    ax1.set_title(title)
    ax1.set_xticklabels(df_pareto[x_label], rotation=45, ha='right')

    # Line chart for cumulative percentage
    ax2 = ax1.twinx()
    ax2.plot(df_pareto[x_label], df_pareto['Porcentagem Cumulativa'], color='red', marker='o', linestyle='--')
    ax2.set_ylabel('Porcentagem Cumulativa (%)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylim(0, 100)

    # Add percentage labels to the cumulative line
    for i, txt in enumerate(df_pareto['Porcentagem Cumulativa']):
        ax2.annotate(f'{txt:.1f}%', (df_pareto[x_label].iloc[i], df_pareto['Porcentagem Cumulativa'].iloc[i]),
                     textcoords="offset points", xytext=(0,10), ha="center")

    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

if __name__ == '__main__':
    analysis_file = 'analysis_by_profile.txt'
    profiles_data = parse_analysis_file(analysis_file)

    # Define themes for problems and suggestions
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

    suggestion_themes = {
        'Melhorar comunicação': ['melhorar comunicação', 'canal de comunicação', 'comunicação eficiente'],
        'Otimizar logística/rotas': ['otimizar logística', 'otimizar rotas', 'entregas por região'],
        'Automação/Sistema': ['automação', 'sistema', 'aplicativo', 'rastreamento'],
        'Treinamento/Capacitação': ['treinamento', 'capacitação', 'orientar'],
        'Planejamento de pedidos': ['planejamento de pedidos', 'antecedência nos pedidos', 'pedidos programados'],
        'Gestão/Controle': ['gestão', 'controle', 'indicadores', 'protocolo'],
        'Aumento de capacidade': ['aumentar capacidade', 'mais colaboradores', 'expandir produção']
    }

    # Analyze problems
    problem_counts_by_profile = {profile: {theme: 0 for theme in problem_themes.keys()} for profile in profiles_data.keys()}
    for profile, questions in profiles_data.items():
        for question, responses in questions.items():
            for response in responses:
                for theme, keywords in problem_themes.items():
                    for keyword in keywords:
                        if re.search(r'\b' + re.escape(keyword) + r'\b', response, re.IGNORECASE):
                            problem_counts_by_profile[profile][theme] += 1
                            break # Count only once per response for a given theme

    # Aggregate problem counts across all profiles
    total_problem_counts = {theme: 0 for theme in problem_themes.keys()}
    for profile, themes_data in problem_counts_by_profile.items():
        for theme, count in themes_data.items():
            total_problem_counts[theme] += count

    # Analyze suggestions
    suggestion_counts = {profile: {theme: 0 for theme in suggestion_themes.keys()} for profile in profiles_data.keys()}
    for profile, questions in profiles_data.items():
        for question, responses in questions.items():
            for response in responses:
                for theme, keywords in suggestion_themes.items():
                    for keyword in keywords:
                        if re.search(r'\b' + re.escape(keyword) + r'\b', response, re.IGNORECASE):
                            suggestion_counts[profile][theme] += 1
                            break # Count only once per response for a given theme

    # Generate charts
    generate_bar_chart(problem_counts_by_profile, 'Frequência de Problemas por Perfil de Ator', 'problemas_por_perfil.png')
    generate_bar_chart(suggestion_counts, 'Frequência de Sugestões de Melhoria por Perfil de Ator', 'sugestoes_por_perfil.png')
    generate_pareto_chart(total_problem_counts, 'Análise de Pareto dos Problemas (Agregado)', 'pareto_problemas_agregado.png', x_label='Problema')

    # Generate Pareto chart for problems by each actor profile
    for profile, problems in problem_counts_by_profile.items():
        # Filter out themes with 0 occurrences for a cleaner Pareto chart
        filtered_problems = {k: v for k, v in problems.items() if v > 0}
        if filtered_problems:
            generate_pareto_chart(filtered_problems, f'Pareto de Problemas para {profile}', f'pareto_problemas_{profile.replace(" ", "_").replace("/", "_")}.png', x_label='Tipo de Problema')

