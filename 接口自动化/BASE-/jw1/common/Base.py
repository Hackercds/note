# 导入json库
import json
# 导入Template类
from string import Template
# 导入re库
import re

# 根据参数匹配内容
def find(data):
    # 判断data类型是否为字典
    if isinstance(data, dict):
        # 对象格式化为str
        data = json.dumps(data)
        # 定义正则匹配规则
        pattern = "\\${(.*?)}" #  提取
        # 按匹配进行查询，把查询的结果放到列表中返回
        return re.findall(pattern, data)
# 进行参数替换
def relace(ori_data, replace_data):
    # 对象格式化为str
    print("dumps 之前",ori_data)
    print("dumps 之前类型", type(ori_data))
    ori_data = json.dumps(ori_data)# 对象格式化为str
    print("dumps 之后", ori_data)
    print("dumps 之后类型", type(ori_data))
    # 处理字符串的类，实例化并初始化原始字符==>支持${token} 变为有效数据
    s = Template(ori_data)
    # 扩展temple的使用  作用 是 s是个模板（包含变量）  replace_data 中的键对应模板时 用值进行替换
    print("模板之后数据",s)
    # 使用新的字符，替换
    return s.safe_substitute(replace_data)
# 测试代码
if __name__ == '__main__':
    # 验证第一个方法
    # 查找id的数据
    red = find({"id": "${id_name}",
                "title": "xiaojiang", "alias": "${heiheihei}", "sex": None})
    print(red)
    # 验证第二个方法
    ori_data = {"authorization": "${jwtoken}"}
    replace_data = {'jwtoken': '111111111'}
    print(relace(ori_data, replace_data))
