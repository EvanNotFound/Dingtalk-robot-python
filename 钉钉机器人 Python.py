import requests
import json
#python 3.8
import time
import hmac
import hashlib
import base64
import urllib.parse

timestamp = str(round(time.time() * 1000))
secret = 'secret here'  #在此处填写机器人的签名
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))


def dingmessage():
# 请求的URL，填写WebHook地址
    webhook = "WEBHOOK HERE"
#构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
}
#构建请求数据
    message ={
         "msgtype": "text",
         "text": 
        {
            "content": "太恐怖了吧"
        },
         "at": {
          "atMobiles":  #At的人的手机号
          [
              
          ],
          "atUserIds":   #At的人的用户id
          [
              
          ],
          "isAtAll": False  #是否At所有人
      }
 }
#对请求的数据进行json封装
    message_json = json.dumps(message)
#发送请求
    info = requests.post(url=webhook+timestamp+"&sign="+sign,data=message_json,headers=header)
#打印返回的结果
    print(info.text)

if __name__=="__main__":
    dingmessage()