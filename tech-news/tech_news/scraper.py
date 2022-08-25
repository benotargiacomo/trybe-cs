from tech_news.database import create_news
from parsel import Selector
import requests
import time


def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"}
        )
    except requests.ReadTimeout:
        return None

    if(response.status_code != 200):
        return None

    return response.text


def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = selector.css('h2.entry-title > a::attr(href)').getall()

    return urls


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css('a.next.page-numbers::attr(href)').getall()

    if len(next_page) == 0:
        return None

    return next_page[0]


def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    news = dict()

    news['url'] = selector.css("head link[rel='canonical']::attr(href)").get()
    news['title'] = selector.css('h1.entry-title::text').get().strip()
    news['timestamp'] = selector.css('li.meta-date::text').get()
    news['writer'] = selector.css('span.author a::text').get()
    news['category'] = selector.css('a.category-style span.label::text').get()
    news['tags'] = selector.css("a[rel='tag']::text").getall()

    comments = selector.css('.post-comments h5.title-block::text').getall()

    if len(comments) == 0:
        news['comments_count'] = 0

    news['comments_count'] = len(comments)

    news['summary'] = ''.join(selector.css(
        'div.entry-content > p:nth-of-type(1) *::text').getall()).strip()

    return news


def get_tech_news(amount):
    # REVISAR
    page = fetch('https://blog.betrybe.com/')
    news_url = scrape_novidades(page)

    news = list()

    while len(news) < amount:
        for url in news_url:
            data = fetch(url)
            new = scrape_noticia(data)

            news.append(new)

    page = fetch(scrape_next_page_link(page))
    news_url = scrape_novidades(data)

    slice = news[:amount]

    create_news(slice)

    return slice
