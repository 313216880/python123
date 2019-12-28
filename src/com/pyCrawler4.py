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
webSourceCode = ' '.join(webSourceCode.split());
re_comment = re.compile('<!--[^>]*-->')
webSourceCode = re_comment.sub('', webSourceCode) 
print(' '.join(webSourceCode.split()))


titleRe=re.compile(r'<div class="bt">(.*?)</div> <div class="more"><a href="(.*?)">更多</a></div>')
#   <a href="(.*?)" title=".*?">(.*?)</a> <span>(.*?)</span>
titles=titleRe.findall(webSourceCode)
print(len(titles))
for title in titles:
    print("=======================分割====================")
    print("url:" + title[0] + "  标题:" + title[1])
    url1 = title[1];
    if './' in url1:
        url1 = url + url1[2:];
    print("url:" + url1 + "  标题:" + title[0])
    
    print("分类:======" + title[0] + "==============url:" + url1)
    
    if "时政要闻" in title[0]:
        break
    webSourceCode1=urllib.request.urlopen(url1).read().decode("utf-8","ignore")
    webSourceCode1 = ' '.join(webSourceCode1.split());
    titleRe1=re.compile(r'<li> <a href="(.*?)" target="_blank" title=".*?">(.*?)</a> <span>(.*?)</span> <div class="clear"></div> </li>')
    titles1=titleRe1.findall(webSourceCode1)
    print(len(titles1))
    for title1 in titles1:
        url2 = url1 + title1[0][2:]
        print("=====下一条========")
        print("url:" + url2 + "  标题:" + title1[1])
        print("发布时间:" + title1[2])
        print("=====详情========")
        if "证监会要闻" in title[0]:
            webSourceCode2=urllib.request.urlopen(url2).read().decode("utf-8","ignore")
            webSourceCode2 = ' '.join(webSourceCode2.split());
            titleRe2=re.compile(r'<div class="title">(.*?)<br> </div>')
            titles2=titleRe2.findall(webSourceCode2)
            print("标题:" + titles2[0])
            print(webSourceCode2)
            contentRe=re.compile(r'<SPAN>(.*?)</SPAN>')
            contents=contentRe.findall(webSourceCode2)
            print("内容:" )
            for content in contents:
                print(content)
        if "新闻发布会" in title[0]:
            webSourceCode2=urllib.request.urlopen(url2).read().decode("utf-8","ignore")
            webSourceCode2 = ' '.join(webSourceCode2.split());
            titleRe2=re.compile(r'<div class="title">(.*?)<br> </div>')
            titles2=titleRe2.findall(webSourceCode2)
            contentRe=re.compile(r'<SPAN>(.*?)</SPAN>')
            contents=contentRe.findall(webSourceCode2)
            print("内容:" )
            for content in contents:
                print(content)
        
        
        
        
        
        
#     imgRe=re.compile(r'src="(.*?\.jpg)"')
#     images=imgRe.findall(webSourceCode)
#     print("图片==============================================================")
#     for image in images:
#         print(image)
#     contentRe=re.compile(r'<p style="text-indent: 2em; font-family: 宋体; font-size: 12pt;">(.*?)</p>')
#     contents=contentRe.findall(webSourceCode)
#     print("内容:" )
#     for content in contents:
#         print(content)
