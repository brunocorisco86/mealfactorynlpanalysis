import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os
from src.utils.logger import get_logger

logger = get_logger(__name__)

class ChartGenerator:
    def __init__(self, analysis_file, plots_dir):
        self.analysis_file = analysis_file
        self.plots_dir = plots_dir
        if not os.path.exists(self.plots_dir):
            os.makedirs(self.plots_dir)

    def generate(self):
        profiles_data = self._parse_analysis_file()

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

        logger.info("Analyzing problems...")
        problem_counts_by_profile = {profile: {theme: 0 for theme in problem_themes.keys()} for profile in profiles_data.keys()}
        for profile, questions in profiles_data.items():
            for question, responses in questions.items():
                for response in responses:
                    for theme, keywords in problem_themes.items():
                        for keyword in keywords:
                            if re.search(r'\b' + re.escape(keyword) + r'\b', response, re.IGNORECASE):
                                problem_counts_by_profile[profile][theme] += 1
                                break
        logger.info("Problem analysis complete.")

        total_problem_counts = {theme: 0 for theme in problem_themes.keys()}
        for profile, themes_data in problem_counts_by_profile.items():
            for theme, count in themes_data.items():
                total_problem_counts[theme] += count

        logger.info("Analyzing suggestions...")
        suggestion_counts = {profile: {theme: 0 for theme in suggestion_themes.keys()} for profile in profiles_data.keys()}
        for profile, questions in profiles_data.items():
            for question, responses in questions.items():
                for response in responses:
                    for theme, keywords in suggestion_themes.items():
                        for keyword in keywords:
                            if re.search(r'\b' + re.escape(keyword) + r'\b', response, re.IGNORECASE):
                                suggestion_counts[profile][theme] += 1
                                break
        logger.info("Suggestion analysis complete.")

        self._generate_bar_chart(problem_counts_by_profile, 'Frequência de Problemas por Perfil de Ator', os.path.join(self.plots_dir, 'problemas_por_perfil.png'))
        self._generate_bar_chart(suggestion_counts, 'Frequência de Sugestões de Melhoria por Perfil de Ator', os.path.join(self.plots_dir, 'sugestoes_por_perfil.png'))
        self._generate_pareto_chart(total_problem_counts, 'Análise de Pareto dos Problemas (Agregado)', os.path.join(self.plots_dir, 'pareto_problemas_agregado.png'), x_label='Problema')

        for profile, problems in problem_counts_by_profile.items():
            filtered_problems = {k: v for k, v in problems.items() if v > 0}
            if filtered_problems:
                self._generate_pareto_chart(filtered_problems, f'Pareto de Problemas para {profile}', os.path.join(self.plots_dir, f'pareto_problemas_{profile.replace(" ", "_").replace("/", "_")}.png'), x_label='Tipo de Problema')

    def _parse_analysis_file(self):
        logger.info(f"Parsing analysis file: {self.analysis_file}")
        with open(self.analysis_file, 'r', encoding='utf-8') as f:
            content = f.read()

        profiles_data = {}
        current_profile = None
        current_question = None

        profile_sections = re.split(r'### Perfil: (.*)\n', content)[1:]
        for i in range(0, len(profile_sections), 2):
            profile_name = profile_sections[i].strip()
            profile_content = profile_sections[i+1]
            profiles_data[profile_name] = {}
            current_profile = profile_name

            question_sections = re.split(r'#### Pergunta: (.*)\n', profile_content)[1:]
            for j in range(0, len(question_sections), 2):
                question_text = question_sections[j].strip()
                responses_content = question_sections[j+1]
                profiles_data[current_profile][question_text] = []

                responses = re.findall(r'- Resposta \d+: (.*)', responses_content)
                profiles_data[current_profile][question_text].extend([r.strip() for r in responses])
        logger.info("Analysis file parsed successfully.")
        return profiles_data

    def _generate_bar_chart(self, data, title, filename):
        logger.info(f"Generating bar chart: {title}")
        df = pd.DataFrame(data).T
        df.plot(kind='bar', figsize=(12, 7))
        plt.title(title)
        plt.ylabel('Frequência')
        plt.xlabel('Perfil do Ator')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        logger.info(f"Bar chart saved to {filename}")

    def _generate_pareto_chart(self, data, title, filename, x_label='Categorias'):
        logger.info(f"Generating Pareto chart: {title}")
        if isinstance(data, dict):
            df_pareto = pd.DataFrame(list(data.items()), columns=[x_label, 'Frequência'])
        else:
            df_pareto = data.copy()

        df_pareto = df_pareto.sort_values(by='Frequência', ascending=False)
        
        df_pareto['Frequência Cumulativa'] = df_pareto['Frequência'].cumsum()
        df_pareto['Porcentagem Cumulativa'] = 100 * df_pareto['Frequência Cumulativa'] / df_pareto['Frequência'].sum()

        fig, ax1 = plt.subplots(figsize=(14, 8))

        ax1.bar(df_pareto[x_label], df_pareto['Frequência'], color='skyblue')
        ax1.set_xlabel(x_label)
        ax1.set_ylabel('Frequência', color='skyblue')
        ax1.tick_params(axis='y', labelcolor='skyblue')
        ax1.set_title(title)
        ax1.set_xticks(range(len(df_pareto)))
        ax1.set_xticklabels(df_pareto[x_label], rotation=45, ha='right')

        ax2 = ax1.twinx()
        ax2.plot(df_pareto[x_label], df_pareto['Porcentagem Cumulativa'], color='red', marker='o', linestyle='--')
        ax2.set_ylabel('Porcentagem Cumulativa (%)', color='red')
        ax2.tick_params(axis='y', labelcolor='red')
        ax2.set_ylim(0, 100)

        for i, txt in enumerate(df_pareto['Porcentagem Cumulativa']):
            ax2.annotate(f'{txt:.1f}%', (df_pareto[x_label].iloc[i], df_pareto['Porcentagem Cumulativa'].iloc[i]),
                         textcoords="offset points", xytext=(0,10), ha="center")

        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        logger.info(f"Pareto chart saved to {filename}")

if __name__ == '__main__':
    chart_generator = ChartGenerator(
        analysis_file='docs/analysis_by_profile.txt',
        plots_dir='plots'
    )
    chart_generator.generate()