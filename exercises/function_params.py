"""
练习: 函数定义与参数

描述：
实现一个计算面积的函数，支持计算长方形和正方形的面积。
"""

def calculate_area(length, width=None):
    """
    计算长方形或正方形的面积
    
    参数:
    - length: 长度
    - width: 宽度（可选，如果不提供则计算正方形面积）
    
    返回:
    - 面积
    """
    if width is None:
        return length * length  # 正方形面积
    return length * width  # 长方形面积 