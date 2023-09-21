# 目标网站：https://quotes.toscrape.com/
# 需求：翻页爬取前4页的名人，名言，标签
import scrapy # 导入 Scrapy 库，用于构建爬虫
from my_scrapy.items import MyScrapyItem # 导入自定义的 Item 类，用于存储爬取的数据

# 定义一个爬虫类
class SpiderSpider(scrapy.Spider):
    # 爬虫的名称
    name = 'spider1'
    # 允许爬取的域名
    allowed_domains = ['quotes.toscrape.com']
    # 页码
    page = 1
    # 链接 url
    base_url = 'https://quotes.toscrape.com/page/{}/'
    # 起始 url
    start_urls = [base_url.format(page)]

    # start_reqeusts 重写的父类方法，优先执行自己
    def start_requests(self):
        # 翻页
        for page in range(1, 5):
            # 确定 url
            url = self.base_url.format(page)
            # 获取数据
            yield scrapy.Request(url, callback=self.parse)

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

        # # 判断页码
        # if self.page <= 4:
        #     # 页码
        #     self.page = self.page + 1
        #     # 获取数据
        #     yield scrapy.Request(self.base_url.format(self.page), callback=self.parse) # callback是回调函数，相当于是发完请求，在那个方法中解析