class student():

    def __init__(self):
        self.name = "zhangsan"


if __name__ == '__main__':
    jw1=student()
    print("学员",jw1.name)
    # 现在学生参加了考试--我想为他增加分数属性
    var_name="fenshu"
    var_res=100
    setattr(jw1,var_name,100)
    print("方式1获取学员分数", jw1.fenshu) # 有警告但是发现能获取
    # 这类属性我们称之为动态参数属性
    #建议获取属性方式
    print("方式2获取学员分数",getattr(jw1,"fenshu","None"))
    # 优势获取不到不会报错 而是返回个None
