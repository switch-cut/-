import pymysql


# 学生登录
def stuLog(name, id):
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    # 使用cursor()方法获取操作游标
    # cursor = db.cursor()
    sql = "select * from students"
    # 转换为字典
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    s = 1
    print(name)
    print(id)
    for i in range(len(data)):
        if (data[i]['Sname']) == name:
            if (data[i]['Sid']) == id:
                s = 0
                print("登录成功-------")
                return 1
                # break
    if (s == 1):
        print("输入有误-------")


# 选课方法
def stuSele(Sid, stuNumber):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor2 = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor3 = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from subject"
    sql2 = "select jcredit from subject where Jid in (select Jid from selection where Sid=" + str(Sid) + ")"
    sql3 = "select Jid from subject"
    cursor.execute(sql)
    cursor2.execute(sql2)
    cursor3.execute(sql3)
    data = cursor.fetchall()
    data2 = cursor2.fetchall()
    data3 = cursor3.fetchall()
    n = 0
    for i in range(len(data2)):
        n += data2[i]['jcredit']
    # print(n)
    db.close()
    j = 0
    for i in data3:
        if stuNumber == i['Jid']:
            j = 1
    print(j)
    # if (stuNumber > len(data) or stuNumber <= 0):
    if j == 0:
        print("课程号输入有误")
        return 0
    elif (n >= 10):
        print("您课程已满，不能进行选课")
        return 1
    else:
        try:
            db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
            cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
            sql1 = "insert into selection values (" + str(Sid) + "," + str(stuNumber) + ")"
            cursor.execute(sql1)
            db.commit()  # 提交到数据库执行
            print("选课成功")
            db.close()
            return 2
        except:
            print("您已经选过该课程了")
            return 3


# 显示个人选课信息
def stuShowSele(Sid):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select Jid,Jname,Jcredit from subject where Jid in (select Jid from selection where Sid=" + str(Sid) + ")"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    db.close()
    return data


# 显示课程表
def stuShowSelevtion():
    db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from subject"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    db.close()
    return data


# 修改个人信息stuUpdate
def stuUpdate(id, name, age, sex, tele):
    try:
        db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        datas = (name, age, sex, tele, id)
        sql = "UPDATE students set Sname = %s,Sage = %s,Ssex = %s,Stele = %s where Sid = %s"
        cursor.execute(sql, datas)
        data = cursor.fetchall()
        db.commit()  # 提交到数据库执行
        print("修改成功")
        db.close()
        return True
    except:
        print('错误')
        return False


def showStuInfor(id):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from students where Sid = " + str(id)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    return data

# ----------------------测试---------------------
# stuShowSele(20001)
# stuShowSelevtion()
# stuSele(20002,7) #选课测试
# stuUpdate(20001,'小孙',21,'男','17658386515')
# showStuInfor(20001)
stuSele(20025, 20)
