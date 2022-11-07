import requests
import bs4
url = 'https://tproger.ru/page/'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}

search = ['С++', 'Python', 'JavaScript', 'IT-команды']

page = 1

for page in range(1,6):
    resp = requests.get(url + str(page)).text
    soup = bs4.BeautifulSoup(resp, features='html.parser')
    articles = soup.find_all('article')


    for article in articles:
        link = article.find(class_="article__link").attrs['href']
        temp_art = bs4.BeautifulSoup(requests.get(link).text, features='html.parser')
        date = temp_art.find(class_='localtime meta__date').text.strip()
        heading = article.find(class_="article__link").text.strip('\n')
        words = heading.split(' ')
        for word in words:
            if word in search:
                print(f'{date} - {heading} - {link}')
    print("перешагнул")
    page += 1
