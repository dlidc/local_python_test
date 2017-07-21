#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('bg')
def bg():
    return  'this is bg for admin'

if __name__ == '__main__':
    app.run(host='0.0.0.0')



##装饰器
##初始化
##关键字参数


