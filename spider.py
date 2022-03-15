import requests
from bs4 import BeautifulSoup
import csv


# 调用函数 write_social_csv() 来进行爬取
def write_social_csv():
    headers = ['area', 'title', 'href']
    with open("test.csv", 'w', encoding='UTF-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(environmental_spider())
        f_csv.writerows(social_spider())
        f_csv.writerows(governance_spider())


def environmental_spider():
    homepage_res = requests.get('http://www.ce.cn/cysc/stwm/')
    homepage_res.encoding = 'gbk'
    # print(homepage_res.status_code)

    homepage_bs = BeautifulSoup(homepage_res.text, 'html.parser')
    li = homepage_bs.find('div', class_='list6')
    # print(li)

    rows = []
    for title in li.find_all('a', href=True):
        if str(title['href'])[0:4] != 'http':
            title['href'] = 'http://www.ce.cn/cysc/stwm' + title['href'][1:]
        line = ['environmental', title.text, title['href']]
        rows.append(line)
    # print(rows)
    return rows


def social_spider():
    homepage_res = requests.get('http://www.ce.cn/xwzx/')
    # print(homepage_res.status_code)
    homepage_res.encoding = 'gbk'

    homepage_bs = BeautifulSoup(homepage_res.text, 'html.parser')
    li = homepage_bs.find('ul', class_='list list5')
    # print(li)

    rows = []
    for title in li.find_all('a', href=True):
        if str(title['href'])[0:4] != 'http':
            title['href'] = 'http://www.ce.cn/xwzx' + title['href'][1:]
        line = ['social', title['title'], title['href']]
        rows.append(line)
    # print(rows)
    return rows


def governance_spider():
    homepage_res = requests.get('http://www.ce.cn/cysc/zljd/index.shtml')
    homepage_res.encoding = 'gbk'
    # print(homepage_res.status_code)

    homepage_bs = BeautifulSoup(homepage_res.text, 'html.parser')
    li = homepage_bs.find('ul', class_='hotnews')
    # print(li)

    rows = []
    for title in li.find_all('a', href=True):
        if str(title['href'])[0:4] != 'http':
            title['href'] = 'http://www.ce.cn/cysc' + title['href'][2:]
        line = ['governance', title.text, title['href']]
        rows.append(line)
    # print(rows)
    return rows


if __name__ == '__main__':
    write_social_csv()
