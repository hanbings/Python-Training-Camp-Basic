"""
练习: 字符串分割

描述：
实现字符串分割相关的功能。
"""

def extract_keywords(text):
    """
    从文本中提取关键词
    
    参数:
    - text: 要处理的文本
    
    返回:
    - 关键词列表
    """
    return text.split()

def parse_csv_line(csv_line):
    """
    解析CSV格式的行
    
    参数:
    - csv_line: CSV格式的字符串
    
    返回:
    - 字段列表
    """
    return csv_line.split(',')

def extract_name_and_domain(email):
    """
    从电子邮件地址中提取用户名和域名
    
    参数:
    - email: 电子邮件地址
    
    返回:
    - (用户名, 域名)元组
    """
    username, domain = email.split('@')
    return username, domain 