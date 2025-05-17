"""
练习: 列表操作

描述：
实现学生列表的增删改操作。
"""

def student_list_operations(student_list, operation, name, new_name=None):
    """
    对学生列表进行操作
    
    参数:
    - student_list: 学生列表
    - operation: 操作类型 ('add', 'remove', 'update')
    - name: 学生姓名
    - new_name: 新的学生姓名（仅用于update操作）
    
    返回:
    - 操作后的学生列表
    """
    if operation == "add":
        student_list.append(name)
    elif operation == "remove":
        if name in student_list:
            student_list.remove(name)
    elif operation == "update":
        if name in student_list:
            index = student_list.index(name)
            student_list[index] = new_name
    return student_list 