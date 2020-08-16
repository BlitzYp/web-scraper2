from bs4 import BeautifulSoup
import random
import aiohttp
import asyncio
import game


def get_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup


async def fetch(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as session:
        html_data: object = await session.text()
        return html_data


async def request(url: str):
    async with aiohttp.ClientSession() as session:
        res = await fetch(session, url)
        return res


def clean(html):
    soup = get_soup(html)
    q: list = soup.find_all(class_='quote')
    data: list = [i.find(class_='text').get_text() for i in q]
    authors: list = [i.find(class_='author').get_text() for i in q]
    return list(zip(data, authors))


def pick_random_quote(quotes):
    rand_page = random.randint(0, len(quotes))
    rand_quote = random.randint(0, rand_page)
    res_q: list = list(quotes[rand_page][rand_quote])
    return res_q[0], res_q[1]


def handle_count(c: int):
    if c:
        return c+1
    return c


async def handle_requests():
    count: int = 1
    res = await request(f"http://quotes.toscrape.com/page/{count}/")
    count = handle_count(count)
    return res


async def get_data():
    data: list = []
    for _ in range(11):
        res = await handle_requests()
        data.append(clean(res))
    return data


def scrape_hint(html: object):
    soup = get_soup(html)
    date = soup.find(class_="author-born-date").get_text()
    location = soup.find(class_='author-born-location').get_text()
    return random.choice([date, location])


async def hints(author: str):
    name: str = author.replace(" ", '-')
    url: str = f'http://quotes.toscrape.com/author/{name}/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data: object = await resp.text()
            res: str = scrape_hint(data)
            return res


async def main():
    res: tuple = await get_data()
    play_game: str = 'yes'
    while not play_game == 'no':
        q: tuple = pick_random_quote(res)
        hint: str = await hints(q[1])
        g = game.handle_game(q, hint)
        print(g)
        play_game: str = str(input("Do you want to play again?(yes/no): "))
    return print("Thanks for playing!")


if __name__ == "__main__":
    asyncio.run(main())
