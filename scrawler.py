# Code by V.Barbosa
import scrapy
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib

# Dados de exemplo com URLs e suas classificações
training_data = [
    {'url': 'https://example.com', 'classification': 'seguro'},
    {'url': 'https://phishing-site.com', 'classification': 'malicioso'},
    # PELO AMOR DE DEUS, ISSO AQUI É PRA IMPLEMENTAR UM .txt, NÃO DEIXAR NO CÓDIGO. 
    # ESTEJAM AVISADOS QUE ESSE CODIGO É APENAS ESTÉTICO.
]

# Extrair conteúdo das páginas e classificações
contents = []
classifications = []
for data in training_data:
    url = data['url']
    content = requests.get(url).content.decode('utf-8')
    classification = data['classification']
    contents.append(content)
    classifications.append(classification)

# Vetorização dos conteúdos usando TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(contents)

# Divisão dos dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, classifications, test_size=0.2, random_state=42)

# Treinamento do modelo SVM
clf = SVC()
clf.fit(X_train, y_train)

# Salvar o modelo treinado
joblib.dump(clf, 'model.joblib')

# Classe para o Spider do Scrapy
class MySpider(scrapy.Spider):
    name = "site_crawler"
    start_urls = [
        'https://example.com',
        # Adicione mais URLs para crawlear aqui
    ]

    def parse(self, response):
        # Extrai o conteúdo da página
        content = response.body.decode(response.encoding)
        
        # Envia o conteúdo para a função de classificação
        classification = self.classify(content)
        
        # Adiciona lógica para criar a blacklist
        if classification == "malicioso":
            self.add_to_blacklist(response.url)
        
        yield {
            'url': response.url,
            'classification': classification
        }

    def classify(self, content):
        # Classificar o conteúdo da página usando o modelo treinado
        X = vectorizer.transform([content])
        classification = clf.predict(X)[0]
        return classification

    def add_to_blacklist(self, url):
        # Adiciona o URL à blacklist (armazenada em um arquivo)
        with open('blacklist.txt', 'a') as file:
            file.write(url + '\n')

# Execução do Spider do Scrapy
process = scrapy.crawler.CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(MySpider)
process.start()
