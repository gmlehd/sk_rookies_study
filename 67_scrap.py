from bs4 import BeautifulSoup
import requests, collections


url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
header_info = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(url, headers=header_info)
soup = BeautifulSoup(r.text, 'lxml')

data = []
tags = soup.select("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div > div > ul > li > div > a")


def scarp_func(tags):
    for tag in tags:
        link_url = {tag.get('href')}   # url 저장
        link_text = tag.get_text()   # text 저장
        data.append(link_text)
        # print(link_text)
        # print(link_url)
        # print("*"*80)
    # print(data)

# print(type(link_url))   # set
# print(type(link_text))  # str

scarp_func(tags)

frequency = collections.Counter(data)
print(frequency)