# 导入datetime库
import datetime

# 导入json库
# 导入MysqlUtil类
from utils.mysqlutil import MysqlUtil

# 初始化mysql工具类
mysql = MysqlUtil()
# 定义获取测试用例类Rd 读取所有的测试用力
class RdTestcase:
    # 需求1：读取指定项目的加载所有的测试用例
    def load_all_case(self, web):
        # 定义sql语句，根据条件web查询test_case_list表中所有测试用例
        sql = f"select * from  jwtest_case_list  where web = '{web}'"
        # 调用工具类方法，获取所有数据
        results = mysql.get_fetchall(sql)
        # 返回结果
        return results
    # 需求2 ：筛选可执行的用例
    def is_run_data(self, web):
        #原始写法
        old_list=[]
        for case in self.load_all_case(web):
            if case['isdel'] == 1:
                old_list.append(case)
        print("老版本写法",old_list)

        # 根据条件isdel==1筛选可执行的测试用例列表
        run_list = [case for case in self.load_all_case(web) if case['isdel'] == 1]
        # 返回可执行测试用例列表
        print("新版本写法",run_list)
        return run_list
    # 需求3 获取配置信息 比如访问的接口服务器地址
    def loadConfkey(self, web, key):
        # 根据web和key,查询test_config相关配置信息
        sql = f"select * from jwtest_config where web='{web}' and key1='{key}'"
        print("sql语句",sql)
        # 调用方法查询1条结果
        results = mysql.get_fetchone(sql)
        print("sql语句查询的结果是",results)
        # 返回结果
        return results
    # 需求3 更新测试结果
    def updateResults(self, response, is_pass, case_id):
        # 获取当前时间
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 更新测试用例执行结果，插入test_result_recorde表
        print(f"jwresponse",response)
        sql = f'insert into  jwtest_result_record(case_id,times,response,result) values ("{case_id}","{current_time}","{str(response)}","{is_pass}")'
        # 执行insert操作
        rows = mysql.sql_execute(sql)
        # 打印日志
        print(sql)
        # 返回更新结果True/False
        return rows

# 测试代码
if __name__ == '__main__':
    jwtestRd = RdTestcase()
    #验证需求2
    res2=jwtestRd.is_run_data("okr-api")
    print(res2)
    #验证需求3
    res3=jwtestRd.loadConfkey("atstudy_okr","url_api")
    print(res3)
    # 验证需求4
    res4 = jwtestRd .updateResults({'success': True,'message': '用户名和密码都不能为空'}, 'True', '4565')
    print(res4)