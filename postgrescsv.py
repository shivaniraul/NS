import psycopg2
con=psycopg2.connect(host='localhost',port="5432",database='db2',user='postgres',password=' ')
cur=con.cursor()
with open('datacust.csv','rb') as f:
    next(f)
    cur.copy_from(f,'customer',sep=',')
con.commit()
print("data into postgres")