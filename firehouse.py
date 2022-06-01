import uuid
from io import BytesIO
import requests
import firebase_admin
from firebase_admin import credentials, firestore, storage


cred = credentials.Certificate('./sk.json')
fire_conf = {
    'storageBucket': 'news-71b1c.appspot.com'
}
firebase_admin.initialize_app(cred, fire_conf)
db = firestore.client()

folder = 'news_images/'
collection_name = 'news'


class FireBoy:
    def __init__(self):
        self.bucket = storage.bucket()
        self.collection = db.collection(collection_name)
        return

    def upload_img(self, url):
        file_key = str(uuid.uuid4())
        img = requests.get(url)
        print(img.headers['Content-Type'])
        try:
            extension = img.headers['Content-Type'].split(';')[0].lower().split('/')[-1].lower()
        except:
            extension = img.headers['Content-Type'].split('/')[-1].lower()
        buffer = BytesIO(img.content)
        file_name = file_key + '.' + extension
        blob = self.bucket.blob(folder + file_name)
        blob.upload_from_file(buffer)
        blob.make_public()
        im_url = blob.public_url
        buffer.close()
        return im_url

    def upload_doc(self, doc):
        res = self.collection.add(doc)
        return res