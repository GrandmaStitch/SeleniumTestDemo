import configparser
import sys
import os
import base64
import requests
from PIL import Image
from io import BytesIO
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class FetchVerifyCode:

    def __init__(self, src_url=None):
        config_path = os.path.abspath(os.path.dirname(
            os.path.dirname(__file__))) + '/config.ini'
        config = configparser.ConfigParser()
        config.read(config_path, encoding='utf-8')
        self.ocr_url = config.get('ocrInfo', 'ocrURL')
        self.ocr_token = config.get('ocrInfo', 'accessToken')
        self.b64_img = None
        if src_url != None:
            self.img = Image.open(requests.get(src_url, stream=True).raw).resize((240, 100))
        else:
            self.img = None

    def im_2_b64(self):
        buff = BytesIO()
        self.img.save(buff, format="PNG")
        img_str = base64.b64encode(buff.getvalue())
        return img_str

    def get_code(self):
        headers = {'host': 'aip.baidubce.com',
                  'Content-Type': 'application/x-www-form-urlencoded'}
        params = {'image': self.b64_img}
        url = self.ocr_url + "?access_token=" + self.ocr_token
        req = requests.post(url, headers=headers, data=params)
        return req.json()['words_result'][0]['words'].replace(' ', '')

    def fetch_token(API_KEY, SECRET_KEY, TOKEN_URL):
        params = {'grant_type': 'client_credentials',
                  'client_id': API_KEY,
                  'client_secret': SECRET_KEY}
        try:
            req = requests.post(TOKEN_URL, params)
            return req.json()['access_token']
        except Exception as e:
            print(e)

    def read_file(image_path):
        # getting image from file
        f = None
        try:
            f = open(image_path, 'rb')
            return f.read()
        except:
            print('read image file fail')
            return None
        finally:
            if f:
                f.close()

    def doOCR(APP_ID, APP_KEY, SECRET_KEY, image_file):
        client = AipOcr(APP_ID, APP_KEY, SECRET_KEY)
        options = {}
        options['language_type'] = 'CHN_ENG'
        options['detect_direction'] = 'true'
        options['detect_language'] = 'true'
        options['probability'] = 'true'
        return client.basicGeneral(image_file, options)


