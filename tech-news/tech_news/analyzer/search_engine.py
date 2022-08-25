from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    news = search_news({'title': {'$regex': title, '$options': 'i'}})

    return [(new['title'], new['url']) for new in news]


def search_by_date(date):
    try:
        is_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Data inválida')
    else:
        f_date = is_date.strftime('%d/%m/%Y')

        news = search_news({'timestamp': f_date})

        return [(new['title'], new['url']) for new in news]


def search_by_tag(tag):
    news = search_news(
        {'tags': {'$elemMatch': {'$regex': tag, '$options': 'i'}}}
    )

    return [(new['title'], new['url']) for new in news]


def search_by_category(category):
    news = search_news({'category': {'$regex': category, '$options': 'i'}})

    return [(new['title'], new['url']) for new in news]
