#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import MySQLdb
import sys,urllib,urllib2
import commands
import pymysql
#避免译码问题
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

app = Flask(__name__)
#以下三行打开uwsgi debug模式
from werkzeug.debug import DebuggedApplication
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
app.debug = True

#测试用       
@app.route('/student', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

#输出表单form    
@app.route('/student/chengji', methods=['GET'])
def chengji_form():
    return render_template("student.html")

#处理表单提交信息，查询数据库，输出结果 
@app.route('/student/query', methods=['POST'])
def query():
    ClassName=request.form['ClassName']
    TestLevel=request.form['TestLevel']
    if ClassName=='': 
        ClassName="22141"
    if TestLevel=='':
        TestLevel='1'
    ##原查询成绩的SQL，改动表结构为课程表，显示时再做行列转换，存为存储过程
    ## sql1=("select a.name,b.* from base as a,chengji as b where a.stuid=b.stuid and a.stuid like '"+ClassName+"%'")
    sql=''
    count=0
    index=[]
    result=[]
    if TestLevel == '1' :
        sql="call SP_QueryData("+ClassName+")"
    else:
        sql="select * from base where stuid like '" + ClassName + "%'"
    ## 原mysqldb库在执行callproc时总报错，改为pymysql库
    ##conn=MySQLdb.connect(host='172.17.0.1',user='root',passwd='root1234',db='students',port=3306,charset='utf8')
    ##cur=conn.cursor()
    conn = pymysql.connect(host='172.17.0.1',user='root', passwd='root1234', db='students', port=3306, charset='utf8')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #cur.callproc('SP_QueryData',(ClassName)) # 参数引用数量总报错.改回execute sql的方式
    count=cur.execute(sql)
    #字段名在index中
    index = cur.description
    #所有记录行在result中
    result=cur.fetchall()
    print "index:",index,"result:",result,"count:",count
    #关闭连接
    conn.commit()
    cur.close()
    conn.close()
    return render_template("student.html",sql=sql,count=count,index=index,result=result)


if __name__ == '__main__':
    app.run()
