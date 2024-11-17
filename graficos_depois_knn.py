import pandas as pd
pd.set_option('display.max_rows', 200)
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

df = pd.read_csv('C:/Users/mvna2/Documents/Programacao/restic36/top_insta_influencers_data_updated.csv')
# Selecionar os 50 primeiros registros para análise
like_comparado_score = df.head(50)

# Criar o gráfico de barras
fig = px.bar(
    like_comparado_score,
    x='channel_info',  # Eixo X
    y='new_post_avg_like',  # Eixo Y
    color='true_influence_score',  # Cor baseada no true_influence_score
    title='Comparação entre o Canal, Likes e o Score Real de Influência',
    labels={
        'channel_info': 'Canal',
        'new_post_avg_like': 'Likes de Novos Posts',
        'true_influence_score': 'Score Real de Influência'
    },
    hover_data={'channel_info': True, 'true_influence_score': True},  # Dados no hover
    height=500
)

fig.update_layout(
    xaxis_tickangle=-45,
    xaxis_title="Canal",
    yaxis_title="Likes de Novos Posts",
    bargap=0.2
)

# Mostrar o gráfico
fig.show()

####################################################################################################

like_comparado_score = df.head(50)

# Criar o gráfico de barras
fig = px.bar(
    like_comparado_score,
    x='channel_info',  # Eixo X
    y='60_day_eng_rate',  # Eixo Y
    color='true_influence_score',  # Cor baseada no true_influence_score
    title='Comparação entre o Canal, Engajamento de 60 Dias e o Score Real de Influência',
    labels={
        'channel_info': 'Canal',
        '60_day_eng_rate': 'Engajamento de 60 Dias',
        'true_influence_score': 'Score Real de Influência'
    },
    hover_data={'channel_info': True, 'true_influence_score': True, '60_day_eng_rate': True},  # Dados no hover
    height=500
)

fig.update_layout(
    xaxis_tickangle=-45,
    xaxis_title="Canal",
    yaxis_title="Engajamento de 60 Dias (%)",
    bargap=0.2
)

# Mostrar o gráfico
fig.show()

##################################################################################################################
# Caminho do arquivo de erro
# Caminho do arquivo de erro
# Caminho do arquivo de erro
error_csv_path = 'C:/Users/mvna2/Documents/Programacao/restic36/knn_error.csv'

# Carregar o arquivo de erro
error_df = pd.read_csv(error_csv_path)

# Verificar as colunas presentes no CSV para garantir o nome correto
print(error_df.columns)

# Criar o gráfico de dispersão com linha para cada métrica usando plotly.graph_objects
fig = go.Figure()

# Adicionar pontos e linhas para cada métrica
for metric in error_df['metric'].unique():
    metric_data = error_df[error_df['metric'] == metric]
    fig.add_trace(go.Scatter(
        x=metric_data['k_neighbors'],
        y=metric_data['mean_test_mse'],
        mode='lines+markers',  # Usar linha com marcadores
        name=metric,  # Nome da métrica
        line=dict(shape='linear')  # Linha reta
    ))

# Adicionar título e rótulos
fig.update_layout(
    title='Taxa de Erro do Modelo KNN',
    xaxis_title='Número de Vizinhos',
    yaxis_title='Erro Médio Quadrático (MSE)',
    legend_title='Métrica de Distância',
    height=500
)

# Mostrar o gráfico
fig.show()