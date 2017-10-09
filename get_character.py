import urllib.request
from bs4 import BeautifulSoup
import http.cookiejar
import csv

ROOT_URL = 'http://www.d-deltanet.com/pc/'
MAIN_PAGE = 'http://www.d-deltanet.com/pc/D0101.do?pmc=22021016'

cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

# メインページ
with opener.open(MAIN_PAGE) as respones:
    html = BeautifulSoup(respones, 'lxml')
    #print(html)
    for mainlinks in html.find_all('a'):
        if '【20】スロ' in mainlinks.text:
            #print(mainlinks)
            suro20 = mainlinks.get('href')
            #print(suro20)

# 機種情報の一覧取得
with opener.open(ROOT_URL + suro20) as respones:
    html = BeautifulSoup(respones, 'lxml')
    #print(html)
    for bajilinks in html.find_all('a'):
        if 'バジリスク〜甲賀忍法帖〜絆 [48]' in bajilinks.text:
            #print(bajilinks)
            bajilink = bajilinks.get('href')
            #print(bajilink)

# 機種項目選択一覧取得
with opener.open(ROOT_URL + bajilink) as respones:
    html = BeautifulSoup(respones, 'lxml')
    opener.addheaders = [('Referer', (ROOT_URL + bajilink))]
    #print(html)
    for bajilist in html.find_all('a'):
        if '大当り一覧' in bajilist.text:
            #print(bajilist)
            bonus = bajilist.get('href')
            #print(bonus)

# 大当たりデータ一覧取得
with opener.open(ROOT_URL + bonus) as respones:
    html = BeautifulSoup(respones, 'lxml')
    #print(html)
    print('------------------------------------')
    table = html.find_all('table')
    #print(table)
    count = 0
    for _, tr_tag in enumerate(table):
        mainlist = []
        sublist = []
        for _, data in enumerate(tr_tag.find_all('td')):
            count += 1
            sublist.append(data.text)
            #print(sublist)
            if count == 5:
                mainlist.append(sublist)
                count = 0
                sublist = []
    print(mainlist)

# csvへ書き出し
with open('sample.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerows(mainlist) # 2次元配列を書き出す
