"""
练习: while循环

描述：
使用while循环查找列表中的第一个偶数。
"""

def find_first_even(numbers):
    """
    查找列表中的第一个偶数
    
    参数:
    - numbers: 数字列表
    
    返回:
    - 第一个偶数，如果没有偶数则返回None
    """
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            return numbers[i]
        i += 1
    return None 