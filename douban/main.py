from scrapy import cmdline
cmdline.execute('scrapy crawl douban_spider -o test.csv'.split())
