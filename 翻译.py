import requests
import json

# json库 处理字符串
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# url 请求的真实地址 注意去掉_o

data = {
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "16142177698026",
    "sign": "041ee6ad96c66adceab357c312359318",
    "lts": "1614217769802",
    "bv": "51c157d16589f89e7109f585b4553d23",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION"
}
# From data 是一个字典

data["i"] = input('请输入: ')

head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.182 Safari/537.36"}

"""
User-Agent 包含我们的系统，浏览器版本号，
           如果使用py这个就是版本号,
           服务器很容易识别出来进而屏蔽我们      
"""

response = requests.post(url=url, data=data, headers=head)
# requests 的标准形式
name = response.json()
print(name["translateResult"][0][0]["tgt"])
