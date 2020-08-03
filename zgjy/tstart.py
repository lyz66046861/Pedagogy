from bs4 import BeautifulSoup
from urllib import request


def has_p_but_no_class(tag):
    return tag.has_attr('p') and not tag.has_attr('class')


# tag.hasattr(class_="offcn_shocont") and not tag.has_attr('style'
url = "http://www.offcn.com/jiaoshi/2020/0707/382993.html"
'''此行可以自行更换代码用来汇集数据'''
response = request.urlopen(url)
html = response.read()
# html = html.decode("html.parser")
bs = BeautifulSoup(html, 'lxml')
article = bs.select(".offcn_shocont")
print(type(article))
print(article)

