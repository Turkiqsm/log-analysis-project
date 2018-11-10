# Logs Analysis - Udacity
### Full Stack Web Development ND
_______________________
## About
in This project, we have the news database that has the logs table that shows the article logs and articles table articles table including author id, and the author table that shows the author details we will extract data such as 
*  What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors? 

## Prerequisites
* [Python 3](https://www.python.org/downloads/release/python-371/) 
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox 3](https://www.virtualbox.org/wiki/Downloads)


## Getting Started 
after installing vagrant you should ```cd``` into vagrant file, then move the ```log-analysis-project/``` inside it, then in the terminal run ```vagrant up```, after it finished run ```vagrant ssh``` now you are inside the Virtual Machine, you should now ```cd /vagrant/``` then ``` cd log-analysis-project/ ``` now you can run the python code by using ```python3 newsdb.py ```
 


### Q1 
a function that returns The most popular three articles of all time 

```python
def Q1():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT title , count(path) as count FROM log JOIN articles on concat( '/article/',articles.slug) = log.path WHERE path like '%article%' GROUP BY title ORDER BY count desc limit 3;")
    res = c.fetchone()
    print("The most popular three articles of all time : ")
    while res:
        print (res[0], end=' = ') , print (res[1])

        res = c.fetchone()
    print('-------------')
    db.close()
```

### Q2
a function that returns The most popular article authors of all time
```python
def Q2():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT authors.name , maxlog.count FROM authors JOIN (SELECT articles.author , count(path) as count FROM log JOIN articles on concat( '/article/',articles.slug) = log.path WHERE path like '%article%' GROUP BY articles.author ORDER BY count desc) as maxlog on authors.id = maxlog.author ORDER BY maxlog.count desc;")    
    res = c.fetchone()
    print("The most popular article authors of all time : ")
    while res:
        print (res[0], end=' = ') , print (res[1])

        res = c.fetchone()
    print('-------------')
    db.close()
```

### Q3 
a function that returns The days did more then 1% of requests lead to errors:

``` python
    def Q3():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT maxi.date , maxi.percent FROM (SELECT DATE(time) as date, count(status), ROUND(100.*count(status)  / total.num,2) AS percent FROM   log JOIN (select DATE(time) as date ,count(status) as num from log  group by DATE(time) ORDER BY date) as total ON total.date = DATE(time) WHERE status != '200 OK'  GROUP BY  DATE(time), total.num ORDER BY total.num desc  ) as maxi WHERE maxi.percent > 1. ;")    
    res = c.fetchone()
    print("The days did more then 1% of requests lead to errors :")
    while res:
        print (res[0], end=' = ') , print (res[1])

        res = c.fetchone()
  
    print('-------------')
    db.close()
```

