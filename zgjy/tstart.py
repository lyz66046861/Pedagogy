from bs4 import BeautifulSoup
from urllib import request
url = "http://www.zgjsks.com/html/2020/edu_0731/472479.html"
'''此行可以自行更换代码用来汇集数据'''
response = request.urlopen(url)
html = response.read()
# html = html.decode("html.parser")
bs = BeautifulSoup(html, 'lxml')
# print(bs.find_all(class_="jxbox clearfix"))
# soup.find_all(attrs={'name':'elements'})//查询name为elements的节点,此处会打印所有子节点
# soup.find_all(class_='element')//由于class在python是一个关键字，所以需要加上下划线
for link in bs.find_all(class_="art_tit"):
    print(link.get_text())
for link in bs.find_all(class_="article"):
    print(link.get_text())
