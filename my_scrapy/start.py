# 使用 cmdline 模块来执行命令行命令
from scrapy import cmdline

# 使用 Scrapy 执行名为 spider 的爬虫
cmdline.execute('scrapy crawl fanyi'.split())

# 使用 Scrapy 执行名为 spider 的爬虫，并将结果保存到 demo.csv 文件中
# cmdline.execute('scrapy crawl spider -o demo.csv'.split())
