from bs4 import BeautifulSoup
from urllib import request
import xlwt
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#descendants
max_page = 1
for value in range(max_page):
    value0 = str(value+2)
    url = "http://www.zgjsks.com/html/jszp/ggjc/edu/" + value0 + ".html"
    '''此行可以自行更换代码用来汇集数据'''
    response = request.urlopen(url)
    html = response.read()
    # html = html.decode("html.parser")
    bs = BeautifulSoup(html, 'lxml')
    def has_class_but_no_id(tag):
        return not tag.has_attr(class_ = "c_tit") and tag.has_attr('href')
    print(bs.find_all(has_class_but_no_id))
    # print(bs.find_all(class_="c_list"))
    # for link in bs.find_all(class_="c_list"):
    #     print(link.get_text(),link.a['href'])




