import pandas as pd
pd.set_option('display.max_rows', 200)
import plotly.express as px
import numpy as np


# 1 passo, ler o csv e fazer as primeiras modificacoes dos dados
# Carregar o arquivo CSV
df = pd.read_csv('C:/Users/mvna2/Documents/Programacao/restic36/top_insta_influencers_data.csv')

# Função para mapear países para códigos de continente
def map_country_to_continent(country):
    country_to_code = {
        # América do Sul
        'Brazil': 1,
        'Uruguay': 2,
        'Colombia': 3,
        
        # América do Norte
        'United States': 20,
        'Canada': 21,
        'Mexico': 22,
        'Puerto Rico': 23,
        'British Virgin Islands': 24,
        'Anguilla': 25,
        
        # Europa
        'Spain': 40,
        'France': 41,
        'Netherlands': 42,
        'United Kingdom': 43,
        'Switzerland': 44,
        'Sweden': 45,
        'Czech Republic': 46,
        'Germany': 47,
        'Italy': 48,
        'Russia': 49,
        
        # Ásia e Oriente Médio
        'India': 60,
        'Turkey': 61,
        'United Arab Emirates': 62,
        "Côte d'Ivoire": 63,
        "Indonesia": 64,
        
        # Oceania
        'Australia': 80,
    }
    return country_to_code.get(country, 0)  # Retorna o código do continente ou 0 se o país não estiver mapeado

# Substituir a coluna 'continent_code' com os códigos mapeados
df['continent_code'] = df['country'].apply(map_country_to_continent)

# Salvar o DataFrame modificado no mesmo arquivo CSV
df.to_csv('C:/Users/mvna2/Documents/Programacao/restic36/top_insta_influencers_data.csv', index=False)

print("Arquivo modificado e salvo com sucesso!")

####################################################################################################################################################################

# Função para converter valores com sufixos 'k', 'm', 'b' para números
def convert_to_numeric(value):
    if isinstance(value, str):
        value = value.lower()
        if 'k' in value:
            return float(value.replace('k', '')) * 1e3  # Mil
        elif 'm' in value:
            return float(value.replace('m', '')) * 1e6  # Milhão
        elif 'b' in value:
            return float(value.replace('b', '')) * 1e9  # Bilhão
    return value  # Caso o valor não tenha sufixo, retornar o valor original

# Colunas a serem convertidas para números
cols_to_convert = ['followers', 'avg_likes', 'new_post_avg_like', 'total_likes', 'posts']

# Aplicar a conversão nas colunas listadas
for col in cols_to_convert:
    df[col] = df[col].apply(convert_to_numeric)

# Sobrescrever o arquivo original com as alterações
df.to_csv('C:/Users/mvna2/Documents/Programacao/restic36/top_insta_influencers_data.csv', index=False)

print("Arquivo modificado e salvo com sucesso!")

#########################################################################################################################

# Selecionar os 25 principais influenciadores
top_25_df = df.head(25)

# Criar o gráfico de barras no Plotly
fig = px.bar(top_25_df, x='channel_info', y=['followers', 'avg_likes'], 
             title='Relação entre Seguidores e Média de Likes para os Top 25 Influenciadores',
             labels={'value': 'Seguidores e Média de Likes', 'channel_info': 'Influenciadores'},
             barmode='group', height=500)

# Ajustar espaçamento e layout para visualização
fig.update_layout(xaxis_tickangle=-45, xaxis_title="Influenciador", yaxis_title="Seguidores e Média de Likes")
fig.update_layout(bargap=0.2)  # Ajuste do espaço entre as barras
fig.show()

###########################################################################################################################

# Selecionar os 50 primeiros registros para visualização
like_comparado_score = df.head(50)

# Criar o gráfico de barras
fig = px.bar(
    like_comparado_score,
    x='channel_info',  # Eixo X
    y='new_post_avg_like',  # Eixo Y
    color='influence_score',  # Cor baseada no influence_score
    title='Comparação entre o Influenciador, Likes e o Score de Influência',
    labels={
        'channel_info': 'Influenciadores',
        'new_post_avg_like': 'Likes de Novos Posts',
        'influence_score': 'Score de Influência'
    },
    hover_data={'channel_info': True, 'influence_score': True},  # Dados no hover
    height=500
)

fig.update_layout(
    xaxis_tickangle=-45,
    xaxis_title="Influenciador",
    yaxis_title="Likes de Novos Posts",
    bargap=0.2  
)

fig.show()


####################################################################################################################################
