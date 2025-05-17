"""
练习: 正则表达式匹配

描述：
使用正则表达式实现邮箱查找、手机号验证和URL提取功能。
"""

import re

def find_emails(text):
    """
    从文本中提取所有邮箱地址
    
    参数:
    - text: 要搜索的文本
    
    返回:
    - 邮箱地址列表
    """
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def is_valid_phone_number(phone):
    """
    验证手机号码是否有效
    
    参数:
    - phone: 要验证的手机号码
    
    返回:
    - 是否有效（布尔值）
    """
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, phone))

def extract_urls(text):
    """
    从文本中提取所有URL
    
    参数:
    - text: 要搜索的文本
    
    返回:
    - URL列表
    """
    pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
    return re.findall(pattern, text) 