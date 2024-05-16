# aicrawler
AI-Powered web scrapping, blacklisting...<br>

1. Os dados de exemplo contendo URLs e suas classificações são definidos na lista training_data.<br>
2. O conteúdo das páginas de exemplo é extraído usando a biblioteca requests.<br>
3. Os dados de treinamento são vetorializados usando TF-IDF.<br>
4. Um modelo de classificação SVM é treinado com os dados de treinamento.<br>
5. O modelo treinado é salvo no arquivo 'model.joblib'.<br>
6. Um spider do Scrapy é definido para fazer o web crawling dos sites.<br>
7. Durante o crawling, cada página é classificada como segura ou maliciosa usando o modelo treinado.<br>
8. Os URLs maliciosos são adicionados à blacklist no arquivo 'blacklist.txt'.<br>
