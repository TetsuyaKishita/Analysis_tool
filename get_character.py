import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen('http://www.d-deltanet.com/pc/D0101.do?pmc=22021016') as response:
    html = response.read()

    print(response.status)
    print(html)
    print(response.geturl())
    #print(response.info())

    print(response.getcode)

    decoded_data = html.decode('Shift_JIS')
    #print(decoded_data)

    page_text = "----text start----"
    for line in response.readlines():
        page_text = page_text + line.decode('Shift_JIS')
    print(page_text)

    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)
