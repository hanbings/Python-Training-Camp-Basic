"""
练习: HTTP请求

描述：
本练习帮助您学习如何使用requests库发送HTTP请求并处理响应。
注意：运行此练习前，请确保已安装requests库（pip install requests）。

请补全下面的函数，实现发送HTTP请求并处理响应的功能。
"""

import requests

def get_website_content(url):
    """
    发送GET请求并获取网站内容
    
    参数:
    - url: 目标网址
    
    返回:
    - 包含状态码、内容和头信息的字典
    """
    try:
        response = requests.get(url)
        return {
            'status_code': response.status_code,
            'content': response.text,
            'headers': dict(response.headers)
        }
    except Exception:
        return {
            'status_code': 0,
            'content': '',
            'headers': {}
        }

def post_data(url, data):
    """
    发送POST请求并获取响应
    
    参数:
    - url: 目标网址
    - data: 要发送的数据（字典）
    
    返回:
    - 包含状态码、响应JSON和成功标志的字典
    """
    try:
        response = requests.post(url, json=data)
        return {
            'status_code': response.status_code,
            'response_json': response.json(),
            'success': response.status_code < 400
        }
    except Exception:
        return {
            'status_code': 0,
            'response_json': {},
            'success': False
        } 