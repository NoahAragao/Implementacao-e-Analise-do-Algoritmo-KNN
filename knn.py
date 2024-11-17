import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Caminho do arquivo CSV
csv_path = 'C:/Users/mvna2/Documents/Programacao/restic36/top_insta_influencers_data.csv'

# Carregar o CSV
df = pd.read_csv(csv_path)

# Remover a coluna 'Unnamed: 10' caso exista
if 'Unnamed: 10' in df.columns:
    df = df.drop(columns=['Unnamed: 10'])

# Converter a coluna '60_day_eng_rate' de string percentual para float
if df['60_day_eng_rate'].dtype == 'object':
    df['60_day_eng_rate'] = df['60_day_eng_rate'].str.replace('%', '').astype(float)

# Tratar valores ausentes
df.fillna(0, inplace=True)

# Pesos para cálculo do true_influence_score
peso_eng_rate = 0.4
peso_avg_like = 0.3
peso_influence = 0.3

# Calcular o true_influence_score com os pesos, usando os valores atualizados de 60_day_eng_rate e new_post_avg_like
df['true_influence_score'] = (
    df['60_day_eng_rate'] * peso_eng_rate +
    df['new_post_avg_like'] * peso_avg_like +
    df['influence_score'] * peso_influence
)

# Normalizar o true_influence_score para a faixa de 0 a 100
score_min = df['true_influence_score'].min()
score_max = df['true_influence_score'].max()
if score_min != score_max:  # Evitar divisão por zero
    df['true_influence_score'] = (df['true_influence_score'] - score_min) / (score_max - score_min) * 100

# Arredondar os valores de 'true_influence_score' para duas casas decimais
df['true_influence_score'] = df['true_influence_score'].round(2)

# Salvar o DataFrame atualizado com a coluna 'true_influence_score' no novo CSV
updated_csv_path = 'C:/Users/mvna2/Documents/Programacao/restic36/top_insta_influencers_data_updated.csv'
df.to_csv(updated_csv_path, index=False)
print(f"Arquivo CSV atualizado com 'true_influence_score' salvo em: {updated_csv_path}")

# Selecionar as features e o target
X = df[['60_day_eng_rate', 'new_post_avg_like', 'influence_score']]
y = df['true_influence_score']

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Parâmetros a serem testados no GridSearchCV
param_grid = {
    'n_neighbors': [1, 3, 5, 7, 9, 11, 15],  # Valores de k a serem testados (aumentado)
    'metric': ['euclidean', 'manhattan', 'chebyshev', 'minkowski', 'cosine']  # Diferentes métricas de distância (aumentado)
}

# Inicializar o modelo KNeighborsRegressor
knn = KNeighborsRegressor()

# Configurar o GridSearchCV para otimizar os parâmetros
grid_search = GridSearchCV(estimator=knn, param_grid=param_grid, scoring='neg_mean_squared_error', cv=5)

# Ajustar o modelo com os melhores parâmetros encontrados
grid_search.fit(X_train, y_train)

# Salvar todos os resultados do GridSearchCV
results = pd.DataFrame(grid_search.cv_results_)

# Extrair os parâmetros relevantes (k_neighbors e metric)
results = results[['param_n_neighbors', 'param_metric', 'mean_test_score']]
results.columns = ['k_neighbors', 'metric', 'mean_test_mse']

# Converter os valores negativos de MSE para positivos
results['mean_test_mse'] = -results['mean_test_mse']

# Salvar os resultados do GridSearchCV em um arquivo CSV
error_csv_path = 'C:/Users/mvna2/Documents/Programacao/restic36/knn_error.csv'
results.to_csv(error_csv_path, index=False)
print(f"Resultados do GridSearchCV salvos em: {error_csv_path}")