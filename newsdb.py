import psycopg2

DBNAME = "news"

def Q1():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT title , count(path) as count FROM log JOIN articles on concat( '/article/',articles.slug) = log.path WHERE path like '%article%' GROUP BY title ORDER BY count desc limit 3;")
    res = c.fetchone()
    print("The most popular three articles of all time : ")
    while res:
        print (res[0], end=' = ') , print (res[1],end=' views \n')

        res = c.fetchone()
    print('-------------')
    db.close()

def Q2():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT authors.name , maxlog.count FROM authors JOIN (SELECT articles.author , count(path) as count FROM log JOIN articles on concat( '/article/',articles.slug) = log.path WHERE path like '%article%' GROUP BY articles.author ORDER BY count desc) as maxlog on authors.id = maxlog.author ORDER BY maxlog.count desc;")    
    res = c.fetchone()
    print("The most popular article authors of all time : ")
    while res:
        print (res[0], end=' = ') , print (res[1] , end=' views \n')

        res = c.fetchone()
    print('-------------')
    db.close()

def Q3():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT maxi.date , maxi.percent FROM (SELECT DATE(time) as date, count(status), ROUND(100.*count(status)  / total.num,2) AS percent FROM   log JOIN (select DATE(time) as date ,count(status) as num from log  group by DATE(time) ORDER BY date) as total ON total.date = DATE(time) WHERE status != '200 OK'  GROUP BY  DATE(time), total.num ORDER BY total.num desc  ) as maxi WHERE maxi.percent > 1. ;")    
    res = c.fetchone()
    print("The days did more then 1% of requests lead to errors :")
    while res:
        print (res[0], end=' = ') , print (res[1] , end=' % \n')

        res = c.fetchone()
  
    print('-------------')
    db.close()


Q1()
Q2()
Q3()
