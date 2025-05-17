"""
练习: 字典操作

描述：
实现一个函数，对学生成绩字典进行增删改查操作。
"""

def student_dict_operations(student_dict, operation, name, score=None):
    """
    对学生成绩字典进行操作
    
    参数:
    - student_dict: 学生成绩字典
    - operation: 操作类型 ('add', 'remove', 'update', 'get')
    - name: 学生姓名
    - score: 学生成绩（可选）
    
    返回:
    - 操作后的字典或查询到的成绩
    """
    if operation == "add":
        student_dict[name] = score
        return student_dict
    elif operation == "remove":
        if name in student_dict:
            del student_dict[name]
        return student_dict
    elif operation == "update":
        if name in student_dict:
            student_dict[name] = score
        return student_dict
    elif operation == "get":
        return student_dict.get(name)
    return student_dict 