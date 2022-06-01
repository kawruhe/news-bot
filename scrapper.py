import justext
import requests


def clean_news(article, news):
    source = article['source']['name']
    title = news['title']
    print(title)
    index = 0
    for i, c in enumerate(reversed(title)):
        if c == "-":
            index = i
            break
    if index > 0:
        index += 1
        news['title'] = title[:-index].strip()
    body = news['body']
    body_len = len(body)
    last_index = body_len - 1
    # for index, para in enumerate(body):
    #     if para['type'] == 0 and index == last_index:
    #         # delete the para from list
    #     elif para['type'] == 0 and body[index+1]['type'] == 0:
    #         # delete para from list
    #     # logics

    return news


def format_news(article_paragraphs):
    content = []
    for paragraph in article_paragraphs:
        if not paragraph.is_boilerplate:
            if paragraph.heading:
                obj = {'type': 0}
            else:
                obj = {'type': 1}
            obj['content'] = paragraph.text
            content.append(obj)
    return content


def get_news_data(key):
    url = "https://newsapi.org/v2/top-headlines?country=in&" \
          "sortBy=publishedAt&apiKey=ed0467faaacd47c8946a90ade0bf42d5"

    response = requests.get(url).json()
    articles = response.get('articles')
    article = articles[5]
    article_url = article['url']
    article_page = requests.get(article_url)
    article_image_url = article['urlToImage']
    article_paragraphs = justext.justext(
        article_page.content, justext.get_stoplist("English"))
    news = {
        'title': article['title'],
        'body': format_news(article_paragraphs),
        'image': article_image_url
    }
    news = clean_news(article, news)
    return news
