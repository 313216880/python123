# encoding: utf-8
'''

Description:
@author: LiuHao
@date 2019年12月18日 下午3:24:01
'''
import urllib.requests
from lxml import etree
import os
import sys
 
def getData(wd):
    # 设置用户代理头
    headers = {
        # 设置用户代理头(为狼披上羊皮)
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    # 构造目标网址
    target_url = "https://www.baidu.com/s?wd="+str(wd)
    # 获取响应
    data = requests.get(target_url, headers = headers)
    # xpath格式化
    data_etree = etree.HTML(data.content)
    # 提取数据列表
    content_list = data_etree.xpath('//div[@id="content_left"]/div[contains(@class, "result c-container")]')
    # 定义返回的字符串
    result = ""
    # 获取标题, 内容, 链接
    for content in content_list:
        result_title = "<标题>  "
        bd_title = content.xpath('.//h3/a')
        for bd_t in bd_title:
            result_title += bd_t.xpath('string(.)')
 
        result_content = "<内容>"
        bd_content = content.xpath('.//div[@class="c-abstract"]')
        for bd_c in bd_content:
            result_content += bd_c.xpath('string(.)')
        try:
            result_link = "<链接>"+str(list(content.xpath('.//div[@class="f13"]/a[@class="c-showurl"]/@href'))[0])
        except:
            result_link = "<链接>: 空"
 
        result_list = [result_title, "\n" , result_content , "\n", result_link]
        for result_l in result_list:
            result += str(result_l)
    return result
 
 
# 保存为文件
def saveDataToFile(file_name, data):
    # 建立文件夹
    if os.path.exists("./data/"):
        pass
    else:
        os.makedirs("./data/")
    with open("./data/"+file_name+".txt", "wb+") as f:
        f.write(data.encode())
 
def main():
    wd = ""
    print(wd)
    try:
        wd = sys.argv[1]
    except:
        pass
 
    if (len(wd) == 0):
        wd = "Hello"
 
    str_data = getData(wd)   
 
    saveDataToFile(wd, str_data)
    print("end")
 
 
if __name__ == '__main__':
    main()