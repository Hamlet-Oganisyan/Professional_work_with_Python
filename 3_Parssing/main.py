from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

UserAgent().chrome

# определяем список ключевых слов
KEYWORDS = ["web", "python", "Привет", "РФ"]
header={'User-Agent': UserAgent().chrome}

base_url = "https://habr.com/"
url = base_url + "ru/all"

response = requests.get(url, headers=header)
data = response.text
soup = BeautifulSoup(data, features="html.parser")
articles = soup.find_all("article")
for article in articles:
    publishigs = article.find(class_="tm-article-body tm-article-snippet__lead")
    publishigs = str(publishigs.text)
    date_publishig = article.find("time").attrs['title']
    title = article.find("h2").find("span").text
    href = article.find(class_ = "tm-article-snippet__title-link").attrs["href"]
    for el in KEYWORDS:
        if el in publishigs:
            print()
            print(f'{ date_publishig}, {title}', {base_url + href})
            print("-"*100)
            print(publishigs)
    