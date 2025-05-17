"""
练习: for循环

描述：
使用for循环计算从1到n的所有整数的和。
"""

def sum_numbers(n):
    """
    计算从1到n的所有整数的和
    
    参数:
    - n: 正整数上限
    
    返回:
    - 从1到n的所有整数的和
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total 