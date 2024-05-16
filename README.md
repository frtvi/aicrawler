# aicrawler
AI-Powered web scrapping, blacklisting...<br>

Os dados de exemplo contendo URLs e suas classificações são definidos na lista training_data.<br>
O conteúdo das páginas de exemplo é extraído usando a biblioteca requests.<br>
Os dados de treinamento são vetorializados usando TF-IDF.<br>
Um modelo de classificação SVM é treinado com os dados de treinamento.<br>
O modelo treinado é salvo no arquivo 'model.joblib'.<br>
Um spider do Scrapy é definido para fazer o web crawling dos sites.<br>
Durante o crawling, cada página é classificada como segura ou maliciosa usando o modelo treinado.<br>
Os URLs maliciosos são adicionados à blacklist no arquivo 'blacklist.txt'.<br>
