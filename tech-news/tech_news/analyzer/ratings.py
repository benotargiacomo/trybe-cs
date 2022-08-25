from tech_news.database import get_collection


def top_5_news():
    db_collection = get_collection()

    news = list(db_collection.find({}).sort([
        ('comments_count', -1),
        ('title', 1)
    ]).limit(5))

    return [(new['title'], new['url']) for new in news]


def top_5_categories():
    """Seu código deve vir aqui"""
