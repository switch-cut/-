import pymysql


# 管理员登录
def admLog(user, psd):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from admin"
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    s = 1
    for i in range(len(data)):
        if (data[i]['Aid']) == user:
            if (data[i]['Apsd']) == psd:
                s = 0
                print("登录成功-------")
                return 1
                # break
    if (s == 1):
        print("输入有误-------")


# 显示全部学生信息
def admShowAllStu():
    db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from students"
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    print(data)
    return data


# 显示全部选课信息
def ShowAllSelection():
    db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select students.*,subject.* from students,selection,subject where students.Sid=selection.Sid and selection.Jid=subject.Jid"
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    print(data)
    return data


# 添加学生
def addStu(name, age, sex, tele):
    try:
        db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        datas = (str(name), str(age), str(sex), str(tele))
        sql = "insert into students (Sname,Sage,Ssex,Stele) values (%s,%s,%s,%s)"
        cursor.execute(sql, datas)
        db.commit()  # 提交到数据库执行
        db.close()
        print('插入成功')
        return True
    except:
        print("输入有误")
        return False


# 删除学生
def delStu(id):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor2 = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql1 = "select Sid from students"
    cursor.execute(sql1)
    data = cursor.fetchall()
    print(data)
    s = False
    for i in data:
        if id == i['Sid']:
            s = True
            break
    if s:
        sql = "delete from students where Sid =" + str(id)
        sql1 = "delete from selection where Sid =" + str(id)
        cursor.execute(sql)
        cursor2.execute(sql1)
        db.commit()  # 提交到数据库执行
        db.close()
        print("删除学生信息成功")
        return True
    else:
        print('没有该学生')
        return False


# 查询某学生的信息
def showStuInfor(id):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from students where Sid = " + str(id)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)

    cursor2 = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql2 = "select Jid,Jname from subject where Jid in (select Jid from selection where Sid=" + str(id) + ")"
    cursor2.execute(sql2)

    data2 = cursor2.fetchall()
    print(data2)
    db.close()
    if len(data) == 0:
        return False
    elif len(data2) == 0:
        return data
    else:
        data = data + data2
        print(data)
        return data


# 添加课程
def addSub(sub):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select Jname from subject"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    s = True
    for i in data:
        if sub == i['Jname']:
            s = False
    if s:
        db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        datas = (sub)
        sql = "insert into subject (Jname,Jcredit) values ( %s ,2)"
        cursor.execute(sql, datas)
        db.commit()  # 提交到数据库执行
        db.close()
        print("添加课程成功")
        return True
    else:
        print("不行")
        return False


# 删除课程
def delsub(id):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql1 = "select Jid from subject"
    cursor.execute(sql1)
    data = cursor.fetchall()
    print(data)
    s = False
    for i in data:
        if id == i['Jid']:
            s = True
            break
    if s:
        sql = "delete from subject where Jid =" + str(id)
        cursor.execute(sql)
        db.commit()  # 提交到数据库执行
        db.close()
        print("删除课程成功")
        return True
    else:
        print('没有该课程')
        return False
    # db = pymysql.connect(host="localhost", user="root", password="123456", db="数据库课程设计-学生选课系统")
    # cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # sql = "delete from subject where id =" + str(id)"
    # cursor.execute(sql)
    # db.commit()  # 提交到数据库执行
    # db.close()
    # print("添加课程成功")


# ------------------------------测试----------------------------
# admShowAllStu()
# addStu('小黄',24,'男','17658386527')
# + ","+ str(age) + ","+ str(sex) + ","+ str(tele) +
showStuInfor(20021)
# delStu(20021)
# ShowAllSelection()#显示全部选课信息
# addSub('数据库')
# delsub(10)
