# Windows10 Python3.9

# インポート
import requests
from bs4 import BeautifulSoup
from PIL import Image
import io
import os

print('実行開始')

# 画像を保存するディレクトリの作成
try:
    os.makedirs('./img')
except FileExistsError:
    pass

# ルートURL
root_url = 'https://scraping-for-beginner.herokuapp.com/'

# サイトにアクセス
url = root_url + 'image'
res = requests.get(url)

# HTMLの構文解析
soup = BeautifulSoup(res.text, 'html.parser')

# img要素の取得
img_tags = soup.find_all('img')

for i, img_tag in enumerate(img_tags): 

    # src属性を取得
    img_src = img_tag['src']

    # 画像のURL
    img_url = root_url + img_src

    # 画像の取得
    img = Image.open(io.BytesIO(requests.get(img_url).content))

    # 画像の保存
    img.save(f'img/{i + 1}.jpg')

print('実行終了')