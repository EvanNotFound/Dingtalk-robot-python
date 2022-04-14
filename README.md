# Dingtalk-robot-python 钉钉机器人 Python 版本

钉钉自定义机器人的python版本，改写自官网开发文档

## 使用方法

首先到钉钉新增自定义机器人

<img width="671" alt="Screen Shot 2022-04-14 at 08 41 58" src="https://user-images.githubusercontent.com/68590232/163291972-1fba7656-307f-4faf-84ab-82442dd21979.png">

然后安全验证方式选择“加签”

<img width="634" alt="Screen Shot 2022-04-14 at 08 42 39" src="https://user-images.githubusercontent.com/68590232/163292038-078de2ad-4560-4172-8deb-2bb42b472618.png">

最后将 `Webhook` 地址和 `加签` 复制下来

分别替换本 Python 脚本中的 `secert here` 和 `WEBHOOK HERE` 地址

便可以直接自定义消息发送到钉钉群中

消息类型详情请见钉钉开发文档 https://open.dingtalk.com/document/group/custom-robot-access

## 代码解析

### 加签部分

```python
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
```
把`timestamp+"\n"+`密钥当做签名字符串，使用`HmacSHA256`算法计算签名，然后进行`Base64 encode`，最后再把签名参数再进行`urlEncode`，得到最终的签名（需要使用`UTF-8`字符集）。

在`secret here`处填写机器人获取到的签名，不要去掉引号

### 请求头部数据部分

```python
def dingmessage():
# 请求的URL，填写WebHook地址
    webhook = "WEBHOOK HERE"
#构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
}
```
在`WEBHOOK HERE`部分填写获取的Webhook地址，不要去掉引号

### 数据输出部分

```python
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
    info = requests.post(url=webhook+"&timestamp="+timestamp+"&sign="+sign,data=message_json,headers=header)
#打印返回的结果
    print(info.text)

if __name__=="__main__":
    dingmessage()
```
消息类型为`text`，内容为`太恐怖了吧`

各种消息类型见 https://open.dingtalk.com/document/group/custom-robot-access

本人对发送请求进行了改动，让`url`等于`webhook`并加上`timestamp`和`sign`签名，每次无需重新获取签名便可发送

## 结尾

还是挺有用的，有很多拓展方式比如邮件转发等
