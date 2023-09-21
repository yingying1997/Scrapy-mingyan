import parsel

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 创建对象
selector = parsel.Selector(html_doc)

# css 选择器
# 解析数据，查找 a 标签
print(selector.css('a').get())
print(selector.css('a').getall())

# xpath语法
print(selector.xpath('//a[@class="sister"]/text()').get())
print(selector.xpath('//a[@class="sister"]/text()').getall())
print(selector.xpath('//a[@class="sister"]/@href').get())
print(selector.xpath('//a[@class="sister"]/@href').getall())

# re
# 注意：sub() 这个方法在这里不能用，建议使用 import re
print(selector.re('.*?<a href="(.*?)" class="sister" id="link1">(.*?)</a>')) # 默认返回的数据类型是list
