'''

Description:   网站爬虫  http://www.gov.cn/guowuyuan/wangyi/index.htm
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
url="http://www.gov.cn/guowuyuan/wangyi/index.htm"
# 该网址的源码(以该网页的原编码方式进行编码，特殊字符编译不能编码就设置ignore)
webSourceCode=urllib.request.urlopen(url).read().decode("utf-8","ignore")
# print(' '.join(webSourceCode.split()))
webSourceCode=' '.join(webSourceCode.split())
titleRe=re.compile(r'<h4 class="fz26 lineh36"><a target="_blank" href="(.*?)">(.*?)</a></h4> <p><a target="_blank" class="color38 fz16 lineh26" href=".*?">(.*?)</a></p> <span class="lineh26 date block fnwr fnwr"> (.*?) </span>')
contentRe=re.compile(r'<p><a target="_blank" class="color38 fz16 lineh26" href=".*?">(.*?)</a></p>')
titles=titleRe.findall(webSourceCode)
content=contentRe.findall(webSourceCode)
print(len(titles))
for title in titles:
    print("=======================分割====================")
#     print(title)
    print("url:" + title[0] + "  标题:" + title[1])
    print("简介:" + title[2])
    print("发布时间:" + title[3])
    print("详情====================")
    webSourceCode=urllib.request.urlopen('http://www.gov.cn' + title[0]).read().decode("utf-8","ignore")
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

# print("内容简介==============================================================")
# for c in content:
#     print(c)
