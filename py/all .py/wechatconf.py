#!usr/bin/env python
from wechat_sdk import WechatConf
conf = WechatConf(
    token='baoshantang',
    appid='wx081a824939a9d544',
    appsecret='8cb47dadc4aa1564b6403db8dc97de6d',
    encrypt_mode='safe',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
    encoding_aes_key='3ShVNG7WLvNJ3ab0xQ6sOP3w9NGiVB59CkTpTRxoXK1'  # 如果传入此值则必须保证同时传入 token, appid
)