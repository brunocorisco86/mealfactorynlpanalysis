
import pandas as pd

def process_data(file_path):
    df = pd.read_excel('/home/brunoconter/Downloads/Análise de Respostas e Diagnóstico de Melhorias na Fábrica(1)/FalhasnaEntregadeRações(1-68).xlsx')
    df["Qual o seu perfil?"].fillna("Não Informado", inplace=True)

    perfis = df["Qual o seu perfil?"].unique()

    analysis_results = {}

    relevant_columns = [
        "Quais tipos de falhas na entrega você já enfrentou? Pode descrever um caso recente?",
        "Quais impactos essas falhas causaram na sua produção?",
        "O que você acredita que poderia ser feito para evitar essas falhas? Traga sugestões de melhoria",
        "Compartilhe um caso de falta/sobra de ração que ocorreu recentemente, pode se um ou mais se houver.",
        "Na sua opinião, porque ocorre falta de ração a campo? ",
        "Na sua opinião, porque tem muita sobra de ração no final do lote? Qual a causa raiz deste problema? ",
        "Que sugestões você tem para melhorar a confiabilidade das entregas? Como poderíamos reduzir estas falhas de entrega? Evitar falta, sobra e descargas erradas",
        "Que sugestões você tem para melhorar a confiabilidade das entregas? Como poderíamos reduzir estas falhas de entrega?",
        "Como as falhas na entrega de ração impactam a saúde e desempenho dos lotes?",
        "O que você acredita que poderia ser feito para reduzir essas falhas? Na sua opinião, como poderíamos melhorar e evitar estes tipos de situação de erro de descarga, falta e sobra de ração?",
        "Na sua opinião, porque tem muita sobra de ração no final do lote? Qual a causa raiz deste problema? 2",
        "Na sua opinião, como poderíamos melhorar o processo e evitar falhas na entrega de ração, sejam elas sobra, falta ou erro na entrega?\n",
        "Quais são os principais motivos de atrasos ou falhas nas entregas?",
        "O que você acredita que poderia ser ajustado para reduzir falhas nas entregas?",
        "Que melhorias você vê como possíveis no processo de planejamento?",
        "Quais são os principais desafios que você enfrenta durante as entregas?",
        "O que você acredita que poderia melhorar na logística das entregas, buscando reduzir erros de entrega, falta e sobra de ração?",
        "Na sua opinião, quais são os principais fatores que contribuem para essas falhas?",
        "Que tipo de ação você acredita que poderia reduzir ou eliminar as falhas nas entregas?",
        "Se pudesse mudar uma coisa no processo para reduzir falhas, qual seria?",
        "Você teria alguma sugestão de melhoria que ainda não foi mencionada?"
    ]

    for perfil in perfis:
        profile_df = df[df["Qual o seu perfil?"] == perfil]
        profile_responses = {}
        for col in relevant_columns:
            if col in profile_df.columns:
                responses = profile_df[col].dropna().astype(str).tolist()
                if responses:
                    profile_responses[col] = responses
        analysis_results[perfil] = profile_responses

    # Save the results to a file for further analysis
    with open("analysis_by_profile.txt", "w", encoding="utf-8") as f:
        for perfil, data in analysis_results.items():
            f.write(f"### Perfil: {perfil}\n")
            if not data:
                f.write("Nenhuma resposta relevante encontrada para este perfil.\n\n")
            else:
                for question, responses in data.items():
                    f.write(f"#### Pergunta: {question}\n")
                    for i, response in enumerate(responses):
                        f.write(f"- Resposta {i+1}: {response}\n")
                    f.write("\n")
            f.write("---\n\n")

    print("Análise por perfil salva em analysis_by_profile.txt")

if __name__ == "__main__":
    file_path = "/home/ubuntu/upload/FalhasnaEntregadeRações(1-68).xlsx"
    process_data(file_path)

