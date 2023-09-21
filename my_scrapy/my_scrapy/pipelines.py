# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 自定义的管道类
class MyScrapyPipeline:
    # 处理 Item 的方法，负责将数据存储到文件中
    def process_item(self, item, spider):
        # 保存数据
        with open('demo.txt', 'a', encoding='utf-8') as f:
            # 将 item 中的 text 字段和 author 字段拼接为一个字符串
            s = item['text'] + item['author']
            # 将拼接后的字符串写入文件，并在末尾添加换行符
            f.write(s + '\n')
        # 返回 item，继续后续的处理过程
        return item