import pymysql
mydb=pymysql.connect(host='localhost',user='root',passwd='shiv@ni123',database="dbsql")
print("connection complete")
mycur=mydb.cursor()
mycur.execute("select * from book")
for i in mycur:
    print(i)