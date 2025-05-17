"""
练习: 面向对象编程基础

描述：
在本练习中，您将学习如何定义类和创建对象，理解面向对象编程的基本概念。

请补全下面的Student类，实现相关方法。
"""

class Student:
    """
    学生类，包含姓名、年龄和成绩属性
    """
    def __init__(self, name, age, grade):
        """
        初始化学生对象
        
        参数:
        - name: 学生姓名
        - age: 学生年龄
        - grade: 学生成绩
        """
        self.name = name
        self.age = age
        self.grade = grade
    
    def print_info(self):
        """
        打印学生信息
        """
        print(f"姓名: {self.name}")
        print(f"年龄: {self.age}")
        print(f"成绩: {self.grade}")
    
    def is_passing(self):
        """
        判断学生是否及格
        
        返回:
        - 是否及格（布尔值）
        """
        return self.grade >= 60

def create_student_example():
    """
    创建并返回一个示例学生对象
    
    返回:
    - Student对象
    """
    student = Student("张三", 18, 85)
    student.print_info()
    return student 