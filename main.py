from bs4 import BeautifulSoup
import random
import aiohttp
import asyncio
from game import handle_game


def get_soup(html):
    soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
    return soup


async def fetch(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as session:
        html_data: object = await session.text()
        return html_data


async def request(url: str):
    async with aiohttp.ClientSession() as session:
        res = await fetch(session, url)
        return res


def clean(html: object):
    soup: BeautifulSoup = get_soup(html)
    q: list = soup.find_all(class_='quote')
    data: list = [i.find(class_='text').get_text() for i in q]
    authors: list = [i.find(class_='author').get_text() for i in q]
    return list(zip(data, authors))


def pick_random_quote(quotes):
    rand_page: int = random.randint(1, 10)
    rand_quote: int = random.randint(0, 5)
    res_q: list = list(quotes[rand_page][rand_quote])
    return res_q[0], res_q[1]


async def handle_requests():
    data: list = []
    count: int = 0
    while count <= 10:
        res = await request(f"http://quotes.toscrape.com/page/{count}/")
        data.append(clean(res))
        count += 1
    return data


def scrape_hint(html: object):
    soup: BeautifulSoup = get_soup(html)
    date: str = soup.find(class_="author-born-date").get_text()
    location: str = soup.find(class_='author-born-location').get_text()
    return date, location


async def hints(author: str):
    name: str = author.replace(" ", '-')
    url: str = f'http://quotes.toscrape.com/author/{name}/'
    resp = await request(url)
    date, location = scrape_hint(resp)
    return date, location


async def main():
    res: tuple = await handle_requests()
    play_game: str = 'yes'
    while not play_game == 'no':
        q: list = pick_random_quote(res)
        date, location = await hints(q[1])
        g = handle_game(q, date, location)
        print(g)
        play_game: str = str(input("Do you want to play again?(yes/no): "))
    return print("Thanks for playing!")


if __name__ == "__main__":
    asyncio.run(main())
