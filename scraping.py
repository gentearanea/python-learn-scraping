import requests
from bs4 import BeautifulSoup


# ターゲットURLのHTMLを取得
target_url = '***'
r = requests.get(target_url) 

# テキストからlxmlに変換
soup = BeautifulSoup(r.text, 'lxml')

# 全てのaタグを取得し表示する
elems = soup.find_all('a')
for elem in elems:
    print(elem.get('href'))