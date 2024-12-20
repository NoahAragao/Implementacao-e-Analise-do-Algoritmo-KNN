# Implementação e Análise do Algoritmo KNN

Este projeto foi feito como avaliação da 9° unidade da residência de software (RESTIC36) voltado no desevolvimento de um algoritmo kNN em um dataset de instagram.
A base de dados foi tirada do site: [https://www.kaggle.com/datasets/surajjha101/top-instagram-influencers-data-cleaned](https://www.kaggle.com/datasets/surajjha101/top-instagram-influencers-data-cleaned).

## Funcionamento do Projeto

Dentro da top_insta_influencers_data.csv existem os seguintes atributos: rank, channel_info, influence_score, posts, followers, avg_likes, 60_day_eng_rate, new_post_avg_like, total_likes, country.

- Rank: Mostra o rank de 1-200 dos tops 200 perfis com mais seguidores de todo o instagram
- Channel Info: Mostra o nome do perfil dos top 200 perfis com mais seguidores de todo o instagram
- Influence Score: Um número de 0 a 100 cálculado para mostrar o quão influente tal perfil do instagram é
- Posts: Quantidade de todos os posts já feitos em cada perfil dos top 200
- Followers: Quantidade de seguidores em cada perfil dos top 200
- Avg Likes: Média total de curtidas em cada post em cada perfil
- 60 Day Eng Rate: Cáculo mostrando o quão popular estava o perfil durante os últimos 60 dias atrás
- New Post Avg Like: Média de curtidas em cada post recente, últimos 60 dias, em cada perfil
- Total Likes: Quantidade total de curtidas já recebidas no perfil
- Country: País de origem do perfil

Ao abrir a pasta, terá 8 arquivos, para executar este projeto, você só precisará de 4:

- graficos_antes_knn.py;
- graficos_depois_knn.py;
- knn.py;
- top_insta_influencers_data.csv

Os outros 4, ou um dos arquivos irá criar depois, como top_insta_influencers_data_updated.csv e knn_error.csv, ou são arquivos para apenas explicar o projeto, como README.md e Relatório Técnico_ Implementação e Análise do Algoritmo k-Nearest Neighbors (kNN) Aplicado ao Instagram.pdf

### Utilização

Para executar este projeto você deve:

1. Baixar a base de dados no link acima

2. Entrar no arquivo graficos_antes_knn.py e mudar o endereço da variavel df para o endereço novo do seu csv da base de dados que você acabou de salvar

3. Executar o arquivo graficos_antes_knn.py

    Assim que você terminar de executar, você terá feito a primeira modificação na sua base de dados, alterando dados para melhor leitura deles para a IA e para os gráficos, além disso, 2 gráficos irão aparecer no seu navegador mostrando alguns insights do database.

    Modificações dos dados:
      - Posts: Float ao invés de String
      - Followers: Float ao invés de String
      - Avg Likes: Float ao invés de String
      - New Post Avg Like: Float ao invés de String
      - Total Likes: Float ao invés de String
      - Country: Integger ao invés de String

4. Mudar o endereço do csv_path com o mesmo endereço do passo 2°, e mude também os: updated_csv_path e do error_csv_path presentes no knn.py.

5. Executar o arquivo knn.py

    Assim que você executar, os arquivos top_insta_influencers_data_updated.csv e knn_error.csv devem ter sido criados ou atualizados.

    Modificações dos dados:
      - 60 Day Eng Rate: Decimal String para Float
      - True Influence Score: true_influence_score criado como Float

6. Entrar no graficos_depois_knn.py e mude o endereço do df para o endereço do top_insta_influencers_data_updated.csv em seu computador, e mude o endereço do error_csv_path para o endereço do knn_error.csv em seu computador.

7. Execute graficos_depois_knn.py

    Assim que terminar de executar, aparecerá em seu navegador 3 gráficos novos mostrando novos insights do database com as alterações feitas no knn.py

## Conclusão

Este projeto tem uma taxa de erro consideravelmente alta chegando aos 27,8%,  indicando limitações no modelo, tanto na base de dados consideravelmente pequena, quanto no próprio algoritmo em si. Para mais informações sobre este projeto, acesse o pdf: Relatório Técnico_ Implementação e Análise do Algoritmo k-Nearest Neighbors (kNN) Aplicado ao Instagram.
