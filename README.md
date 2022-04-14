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

消息类型详情请见钉钉开发文档
https://open.dingtalk.com/document/group/custom-robot-access
