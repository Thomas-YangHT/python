#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask
from flask import request
import MySQLdb
import sys,urllib,urllib2
import commands

app = Flask(__name__)

text_content = '''
 <html>  
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <title>CHENGJI Query</title>
  <link rel='stylesheet' href='css/jquery-ui.css'>
  <link rel='stylesheet' href='css/style.css'>
  <script src='js/jquery-1.12.4.js'></script>
  <script src='js/jquery-ui.js'></script>

 <script type='text/javascript'> 
 function altRows(id){           
    if(document.getElementsByTagName){          
        var table = document.getElementById(id);  
        var rows = table.getElementsByTagName(\"tr\");       
        for(i = 0; i < rows.length; i++){          
            if(i % 2 == 0){                        
                rows[i].className = 'evenrowcolor';
            }else{                                 
                rows[i].className = 'oddrowcolor'; 
            }      
        }          
    }              
 }               

 window.onload=function(){ 
    altRows('alternatecolor');
 } 
 </script>


<!-- CSS goes in the document HEAD or added to your external stylesheet --> 
 <style type='text/css'> 
 table.altrowstable {
    font-family: verdana,arial,sans-serif;
    font-size:11px;
    color:#333333;
    border-width: 1px;
    border-color: #a9c6c9;
    border-collapse: collapse;
 }
 table.altrowstable th {
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #a9c6c9;
    background-color:#ccd4d4;
 }
 table.altrowstable td {
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #a9c6c9;
 }
 .oddrowcolor{
    background-color:#d4e3e5;
 }
 .evenrowcolor{
 /* background-color:#c3dde0; */
 background-color:#ffffff;
 }
 .shiny-blue {
   background-color: #759ae9;
   background-image: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #759ae9), color-stop(50%, #376fe0), color-stop(50%, #1a5ad9), color-stop(100%, #2463de));
   background-image: -webkit-linear-gradient(top, #759ae9 0%, #376fe0 50%, #1a5ad9 50%, #2463de 100%);
   background-image: -moz-linear-gradient(top, #759ae9 0%, #376fe0 50%, #1a5ad9 50%, #2463de 100%);
   background-image: -ms-linear-gradient(top, #759ae9 0%, #376fe0 50%, #1a5ad9 50%, #2463de 100%); 
   background-image: -o-linear-gradient(top, #759ae9 0%, #376fe0 50%, #1a5ad9 50%, #2463de 100%);
   background-image: linear-gradient(top, #759ae9 0%, #376fe0 50%, #1a5ad9 50%, #2463de 100%);
   border-top: 1px solid #1f58cc;
   border-right: 1px solid #1b4db3;
   border-bottom: 1px solid #174299; 
   border-left: 1px solid #1b4db3; 
   border-radius: 4px; 
   -webkit-box-shadow: inset 0 0 2px 0 rgba(57, 140, 255, 0.8);
   box-shadow: inset 0 0 2px 0 rgba(57, 140, 255, 0.8); 
   color: #fff; 
   font: bold 12px/1 'helvetica neue', helvetica, arial, sans-serif;
   padding: 7px 0; 
   text-shadow: 0 -1px 1px #1a5ad9;
   width:50px;
    }
 </style>
 </head>
<body style='margin:0 auto;text-align:center;'>
</br>";
 <form id='form' name='form' method='post' action='/student/query'>
 班级: <input type='text' name='ClassName' id='ClassName' value='1807'>
 项目: <input type='text' name='TestLevel' id='TestLevel' value='1'>
 0-学生基本信息；1-计算机基础成绩；
   <input class='shiny-blue' type='submit' name='Submit' value='提交' />
 </form>
'''
       
@app.route('/student', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

    
@app.route('/student/chengji', methods=['GET'])
def chengji_form():
    return text_content

              
@app.route('/student/query', methods=['POST'])
def query():
    ClassName=request.form['ClassName']
    TestLevel=request.form['TestLevel']
    try:
        conn=MySQLdb.connect(host='172.16.254.110',user='yanght',passwd='yanght',db='students',port=3306,charset='utf8')
        cur=conn.cursor()
        sql1=("select a.name,b.* from base as a,chengji as b where a.stud_no=b.stud_no and a.stud_no like '%s\%'" % ClassName)
        sql=("select * from base order by stud_no")
        if TestLevel==1 :
            sql=sql1
        ret=sql
        count=cur.execute(sql)
        ret+= 'there has %s rows record' % count
        if count != 0 :
            result=cur.fetchall()

        for row in result:
            for i in row:
                ret+= "%s" % i
        #   if type(x) != None:
        #       content+=str(x)+';'
        #   else:
        #       content+='empty'+';'
                
        #index = cur.description
        #result = []
        #for res in cur.fetchall():
        #row = {}
        #for i in range(len(index)-1):
        #    row[index[i][0]] = res[i]
        #    result.append(row)
        conn.commit()
        cur.close()
        conn.close()
        text_content+=ret
    except MySQLdb.Error,e:
        return "Mysql Error %d: %s" % (e.args[0], e.args[1])
    #return '<h1>Home</h1>'
    #print "ClassName:%s" % ClassName
    #res1=chengji_form()
    #res2=GET_DATA()
    return text_content




if __name__ == '__main__':
    app.run()
