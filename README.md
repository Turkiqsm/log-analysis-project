{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf100
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red0\green0\blue0;\red70\green137\blue204;
\red23\green23\blue23;\red202\green202\blue202;\red212\green214\blue154;\red140\green211\blue254;\red194\green126\blue101;
\red167\green197\blue152;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\csgray\c0\c0;\cssrgb\c33725\c61176\c83922;
\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;\cssrgb\c86275\c86275\c66667;\cssrgb\c61176\c86275\c99608;\cssrgb\c80784\c56863\c47059;
\cssrgb\c70980\c80784\c65882;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10700\viewh18300\viewkind0
\deftab720
\pard\pardeftab720\sl360\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 # NEWS \
\
\
NEWS is a database has articles and authors and logs.\
## newsdb.py\
\
### Q1 \
a function that returns The most popular three articles of all time \
\
```python\
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb5 def\cf6 \strokec6  \cf7 \strokec7 Q1\cf6 \strokec6 ():\cb1 \
\cb5     db = psycopg2.connect(\cf8 \strokec8 database\cf6 \strokec6 =DBNAME)\cb1 \
\cb5     c = db.cursor()\cb1 \
\cb5     c.execute(\cf9 \strokec9 "SELECT title , count(path) as count FROM log JOIN articles on concat( '/article/',articles.slug) = log.path WHERE path like '\cf4 \strokec4 %a\cf9 \strokec9 rticle%' GROUP BY title ORDER BY count desc limit 3;"\cf6 \strokec6 )\cb1 \
\cb5     res = c.fetchall()\cb1 \
\cb5     \cf7 \strokec7 print\cf6 \strokec6 (res)\cb1 \
\cb5     db.close()\cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec4 \
```\
\
### Q2\
a function that returns The most popular article authors of all time\
```python\
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb5 def\cf6 \strokec6  \cf7 \strokec7 Q2\cf6 \strokec6 ():\cb1 \
\cb5     db = psycopg2.connect(\cf8 \strokec8 database\cf6 \strokec6 =DBNAME)\cb1 \
\cb5     c = db.cursor()\cb1 \
\cb5     c.execute(\cf9 \strokec9 "SELECT authors.name , maxlog.count FROM authors JOIN (SELECT articles.author , count(path) as count FROM log JOIN articles on concat( '/article/',articles.slug) = log.path WHERE path like '\cf4 \strokec4 %a\cf9 \strokec9 rticle%' GROUP BY articles.author ORDER BY count desc) as maxlog on authors.id = maxlog.author ORDER BY maxlog.count desc;"\cf6 \strokec6 )    \cb1 \
\cb5     res = c.fetchall()\cb1 \
\cb5     \cf7 \strokec7 print\cf6 \strokec6 (res)\cb1 \
\cb5     db.close()\cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec4 \
```\
\
### Q3 \
a function that returns The days did more then 1% of requests lead to errors:\
\
``` python\
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb5 def\cf6 \strokec6  \cf7 \strokec7 Q3\cf6 \strokec6 ():\cb1 \
\cb5     db = psycopg2.connect(\cf8 \strokec8 database\cf6 \strokec6 =DBNAME)\cb1 \
\cb5     c = db.cursor()\cb1 \
\cb5     c.execute(\cf9 \strokec9 "SELECT maxi.date , maxi.percent FROM (SELECT DATE(time) as date, count(status), ROUND(100.*count(status)  / total.num,2) AS percent FROM   log JOIN (select DATE(time) as date ,count(status) as num from log  group by DATE(time) ORDER BY date) as total ON total.date = DATE(time) WHERE status != '200 OK'  GROUP BY  DATE(time), total.num ORDER BY total.num desc  ) as maxi WHERE maxi.percent > 1. ;"\cf6 \strokec6 )    \cb1 \
\cb5     res = c.fetchall()\cb1 \
\cb5     \cf7 \strokec7 print\cf6 \strokec6 (res[\cf10 \strokec10 0\cf6 \strokec6 ])\cb1 \
\cb5     db.close()\cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec4 \
```\
\
}