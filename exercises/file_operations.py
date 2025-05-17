"""
练习: 文件处理

描述：
本练习帮助您学习如何在Python中进行文件的读取和写入操作。

请补全下面的函数，实现文件的读取和写入功能。
"""

def read_file(file_path):
    """
    读取文件内容
    
    参数:
    - file_path: 文件路径
    
    返回:
    - 文件内容（字符串）
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return ""

def write_file(file_path, content):
    """
    写入内容到文件
    
    参数:
    - file_path: 文件路径
    - content: 要写入的内容
    
    返回:
    - 是否写入成功（布尔值）
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception:
        return False 