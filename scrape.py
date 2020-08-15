from bs4 import BeautifulSoup
import requests

def get_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def fire_requests():
    count = '/page/1/'
    data: list = []
    res= requests.get(f"http://quotes.toscrape.com{count}")
    while True:
        html = res.text
        soup = get_soup(html)
        data.append(html)
        pages = soup.find(class_='next')
        if pages:
            count = pages.find('a')['href']
            res= requests.get(f"http://quotes.toscrape.com{count}")
            continue
        return data

def clean(html):
    soup = get_soup(html)
    q: list = soup.find_all(class_= 'quote')
    data: list = [i.find(class_='text').get_text() for i in q]
    authors: list = [i.find(class_='author').get_text() for i in q]
    return list(zip(data,authors))


def main():
    res = fire_requests()
    return res

print(main())