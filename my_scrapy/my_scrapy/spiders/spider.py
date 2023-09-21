# 目标网站：https://quotes.toscrape.com/
# 需求：翻页爬取每页的名人，名言，标签
import scrapy # 导入 Scrapy 库，用于构建爬虫
from my_scrapy.items import MyScrapyItem # 导入自定义的 Item 类，用于存储爬取的数据

# 定义一个爬虫类
class SpiderSpider(scrapy.Spider):
    # 爬虫的名称
    name = 'spider'
    # 允许爬取的域名
    allowed_domains = ['quotes.toscrape.com']
    # 起始 url
    start_urls = ['https://quotes.toscrape.com/']

    # 解析函数，处理响应并提取数据
    def parse(self, response):
        # 使用 XPath 选取所有 class 为 quote 的 div 元素
        divs = response.xpath('//div[@class="quote"]')
        # 遍历每个 div 元素
        for div in divs:
            # 创建一个 MyScrapyItem 实例，用于存储爬取的数据
            item = MyScrapyItem()
            # 获取名言文本
            item['text'] = div.xpath('.//span[1]/text()').get()
            # 获取名人文本
            item['author'] = div.xpath('.//span[2]/small[1]/text()').get()
            # 获取标签文本
            item['tags'] = div.xpath('.//div[1]/a/text()').getall()
            # 返回 item，将其传递给引擎
            yield item

        # 翻页爬取，获取下一页按钮
        next = response.xpath('//li[@class="next"]/a/@href').get()
        # 拼接下一页链接
        # 方法一：
        # url = self.start_urls[0] + next
        # 方法二：
        url = response.urljoin(next)
        # 发起一个新的请求，url 为 next 的绝对 url，并将响应交给 parse 方法处理
        yield scrapy.Request(url, callback=self.parse)