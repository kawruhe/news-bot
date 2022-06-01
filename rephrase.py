import requests
paraphrase_url = 'https://rewriter-paraphraser-text-changer-multi-language.p.rapidapi.com/rewrite'


def get_paraphrased_sentence(paragraph):
    payload = {
        "language": "en",
        "strength": 3,
        "text": paragraph
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Host": "rewriter-paraphraser-text-changer-multi-language.p.rapidapi.com",
        "X-RapidAPI-Key": "8cc7491dbamsh21dc8b520329546p1eb000jsnb099c6381cba"
    }

    response = requests.post(paraphrase_url, json=payload, headers=headers)
    return response.json()['rewrite']


def rephrase_article(article):
    for item in article:
        item['content'] = get_paraphrased_sentence(item['content'])
    return article
