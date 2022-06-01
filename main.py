from firehouse import FireBoy
from rephrase import rephrase_article
from scrapper import get_news_data

f_boy = FireBoy()

news = get_news_data("plane")
print(news)
# im_url = f_boy.upload_img(news['image'])
# news['image'] = im_url
# news['body'] = rephrase_article(news['body'])

# f_boy.upload_doc(news)





