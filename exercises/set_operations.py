"""
练习: 集合操作

描述：
实现集合的基本操作（并集、交集、差集）。
"""

def student_set_operations(set1, set2, operation):
    """
    对两个学生集合进行操作
    
    参数:
    - set1: 第一个学生集合
    - set2: 第二个学生集合
    - operation: 操作类型 ('union', 'intersection', 'difference')
    
    返回:
    - 操作后的集合
    """
    if operation == "union":
        return set1 | set2
    elif operation == "intersection":
        return set1 & set2
    elif operation == "difference":
        return set1 - set2
    return set()