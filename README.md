# scrapy_douban
功能：爬取https://movie.douban.com/top250 ，使用随机useragent，保存到mongodb和本地csv。  
慕课网视频链接：https://www.imooc.com/video/17523  

### 环境：  
centos7  
python3.6.5  
gcc 4.8.5    
Scrapy==2.1.0
Twisted==20.3.0
pymongo==3.10.1
pip==20.1

### 启动：  
`python main.py`  

### 结果：  
数据库有数据，douban文件夹下生成csv文件  

### tips:  
pip install Scrapy 可能连带着Twisted安装，就不用再pip install Twisted  
建议先更新pip再install其他  
数据库认证  
csv改编码格式  
