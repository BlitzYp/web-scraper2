from bs4 import BeautifulSoup
import requests
import random

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


def pick_random_quote(quotes):
    i: int = random.randint(0, len(quotes[0]))
    res_q: list = list(quotes[0][i])
    return res_q[0]

def main():
    res = fire_requests()
    data: list = [clean(i) for i in res]
    q = pick_random_quote(data)
    return q

print(main())