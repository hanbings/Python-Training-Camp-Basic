"""
练习: if-elif-else 条件语句

描述：
根据分数判断成绩等级。
"""

def check_grade(score):
    """
    根据分数判断成绩等级
    
    参数:
    - score: 分数（0-100）
    
    返回:
    - 成绩等级（优秀/良好/中等/及格/不及格）
    """
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 70:
        return "中等"
    elif score >= 60:
        return "及格"
    else:
        return "不及格" 