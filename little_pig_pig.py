import pymysql as mysql
import pandas


# 函数名: mysql_connect
# def:表示后面的东西是函数
def mysql_connect():
    # 连接数据库
    db = mysql.connect(host='192.168.199.130',
                       user='root',
                       password='123456',
                       database='information_schema',
                       charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    print("数据库连接成功！")

    return cursor

# 查询语句
def select_tables(cursor, table_name):
    try:
        sql = "select * from {}".format(table_name)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data)
    except Exception:
        print("查询失败")


# 代码从main函数开始执行
if __name__ == "__main__":
    cursor = mysql_connect()
    select_tables(cursor, 'CHARACTER_SETS')
    create_tables(cursor, 'test_table')
