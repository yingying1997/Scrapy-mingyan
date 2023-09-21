import scrapy # 导入 Scrapy 库，用于构建爬虫

# 定义 FanyiSpider 类，继承自 scrapy.Spider 类
class FanyiSpider(scrapy.Spider):
    # 爬虫的名称
    name = 'fanyi'
    # 允许爬取的域名
    allowed_domains = ['fanyi.so.com']
    # 起始 url
    start_urls = ['https://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query=hello']
    # post 请求携带参数
    data = {
        'eng': '1',
        'ignore_trans': '0',
        'query': 'hello',
    }

    # 定义 start_requests 方法，用于生成初始请求，重写的父类方法
    def start_requests(self):
        # 使用 FormRequest 发送 post 请求（FormRequest 类是继承 Request 类）
        yield scrapy.FormRequest(self.start_urls[0], callback=self.parse, formdata=self.data)

    # 解析函数，处理响应并提取数据
    def parse(self, response):
        # 打印请求头和响应状态码
        # print(response.request.headers, response.status)
        # 打印响应数据中的翻译结果
        print(response.json()['data']['fanyi'])
        # 输入翻译内容
        query = input("请输入翻译内容")
        # post 请求携带参数
        data = {
            'eng': '1',
            'ignore_trans': '0',
            'query': query,
        }
        # 发送新的 post 请求并将响应交给 parse 方法处理
        yield scrapy.FormRequest(self.start_urls[0], callback=self.parse, formdata=data)