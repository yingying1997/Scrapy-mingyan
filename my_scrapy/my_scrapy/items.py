# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy # 导入Scrapy库，用于构建爬虫

# 自定义的Item类，用于存储爬取的数据
class MyScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 名言
    text = scrapy.Field() # 用于存储名言文本内容的字段
    # 名人
    author = scrapy.Field() # 用于存储名人文本内容的字段
    # 标签
    tags = scrapy.Field() # 用于存储标签文本内容的字段
