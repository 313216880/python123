'''

Description:   网站爬虫  http://sousuo.gov.cn/column/45066/0.htm
@author: LiuHao
@date 2019年12月10日 上午9:35:17
'''
# 导入urllib下的request模块
import urllib.request
# 导入正则匹配包
import re

# -*- encoding:utf-8 -*-
# 步骤
# 1.确定要爬取数据的网址
# 2.获取该网址的源码
# 3.使用正则表达式去匹配网址的源码（匹配所需要的数据类型）
# 4.将爬取的数据保存至本地或者数据库

# 确定要爬取数据的网址
url="http://www.csrc.gov.cn/pub/newsite/zjhxwfb/"
# 该网址的源码(以该网页的原编码方式进行编码，特殊字符编译不能编码就设置ignore)
webSourceCode=urllib.request.urlopen(url).read().decode("utf-8","ignore")
print(' '.join(webSourceCode.split()))
webSourceCode = ' '.join(webSourceCode.split())
titleRe=re.compile(r'<h4>[\s\S]*?<a href="(.*?)" target="_blank">(.*?)</a>[\s\S]*?<span class="date">(.*?) </span>[\s\S]*?</h4>')
   
titles=titleRe.findall(webSourceCode)
print(len(titles))
for title in titles:
    print("=======================分割====================")
    print("url:" + title[0] + "  标题:" + title[1] + "  发布时间:" + title[2])
    print("详情====================")
    webSourceCode=urllib.request.urlopen(title[0]).read().decode("utf-8","ignore")
    titleRe1=re.compile(r'<h1>([\s\S]*?)</h1>')
    titles1=titleRe1.findall(webSourceCode)
    for title in titles1:
        print("标题:" + title)
    imgRe=re.compile(r'src="(.*?\.jpg)"')
    images=imgRe.findall(webSourceCode)
    print("图片==============================================================")
    for image in images:
        print(image)
    contentRe=re.compile(r'<p style="text-indent: 2em; font-family: 宋体; font-size: 12pt;">(.*?)</p>')
    contents=contentRe.findall(webSourceCode)
    print("内容:" )
    for content in contents:
        print(content)
