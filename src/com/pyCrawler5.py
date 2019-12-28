'''

Description:   网站爬虫  http://www.customs.gov.cn/customs/xwfb34/302425/index.html
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
url="http://www.pbc.gov.cn/rmyh/105208/index.html"

headers = {
    'Cookie': '__guid=30183481.4126542558894958000.1576648734948.7078; wzws_cid=1ef12576161902f8be87de077f230114a5fc50cb0f8cd9e2b90d9478b24df565f51751615852b1792b3223baf86b1b8decf0344315b0850fdc8c5eaeee0b5e37a30b1154304997161af1f935253b9eeb; monitor_count=31',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}
req=urllib.request.Request(url=url,headers=headers)
# 该网址的源码(以该网页的原编码方式进行编码，特殊字符编译不能编码就设置ignore)
webSourceCode=urllib.request.urlopen(req).read().decode("utf-8","ignore")
# webSourceCode=urllib.request.urlopen(url).read().decode("utf-8","ignore")
print(webSourceCode)
webSourceCode = ' '.join(webSourceCode.split());
print(' '.join(webSourceCode.split()))

# 
# titleRe=re.compile(r'<div class="bt">(.*?)</div> <div class="more"><a href="(.*?)">更多</a></div>')
# #   <a href="(.*?)" title=".*?">(.*?)</a> <span>(.*?)</span>
# titles=titleRe.findall(webSourceCode)
# print(len(titles))
# for title in titles:
#     print("=======================分割====================")
#     print("url:" + title[0] + "  标题:" + title[1])
#     url1 = title[1];
#     if './' in url1:
#         url1 = url + url1[2:];
#     print("url:" + url1 + "  标题:" + title[0])
#     
#     print("分类:======" + title[0] + "==============url:" + url1)
#     
#     if "时政要闻" in title[0]:
#         break
#     webSourceCode1=urllib.request.urlopen(url1).read().decode("utf-8","ignore")
#     webSourceCode1 = ' '.join(webSourceCode1.split());
#     titleRe1=re.compile(r'<li> <a href="(.*?)" target="_blank" title=".*?">(.*?)</a> <span>(.*?)</span> <div class="clear"></div> </li>')
#     titles1=titleRe1.findall(webSourceCode1)
#     print(len(titles1))
#     for title1 in titles1:
#         url2 = url1 + title1[0][2:]
#         print("=====下一条========")
#         print("url:" + url2 + "  标题:" + title1[1])
#         print("发布时间:" + title1[2])
#         print("=====详情========")
#         if "证监会要闻" in title[0]:
#             webSourceCode2=urllib.request.urlopen(url2).read().decode("utf-8","ignore")
#             webSourceCode2 = ' '.join(webSourceCode2.split());
#             titleRe2=re.compile(r'<div class="title">(.*?)<br> </div>')
#             titles2=titleRe2.findall(webSourceCode2)
#             print("标题:" + titles2[0])
#             print(webSourceCode2)
#             contentRe=re.compile(r'<SPAN>(.*?)</SPAN>')
#             contents=contentRe.findall(webSourceCode2)
#             print("内容:" )
#             for content in contents:
#                 print(content)
#         if "新闻发布会" in title[0]:
#             webSourceCode2=urllib.request.urlopen(url2).read().decode("utf-8","ignore")
#             webSourceCode2 = ' '.join(webSourceCode2.split());
#             titleRe2=re.compile(r'<div class="title">(.*?)<br> </div>')
#             titles2=titleRe2.findall(webSourceCode2)
#             contentRe=re.compile(r'<SPAN>(.*?)</SPAN>')
#             contents=contentRe.findall(webSourceCode2)
#             print("内容:" )
#             for content in contents:
#                 print(content)
#         
#         
#         
#         
        
        
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
