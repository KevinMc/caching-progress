# -*- encoding: utf-8 -*-
import sqlite3 as lite
import unicodedata, math, itertools
from dateutil import parser
from datetime import datetime
import json

con = lite.connect('sqlite.db3')


li = []


with con:
    con.row_factory = lite.Row
    cur = con.cursor()
    cur.execute('select Code,Name,County,State,FoundByMeDate, lLogId from caches inner join logs on lParent = Code where lBy = "Yaten" and Country = "United States" and lType IN ("Found it","Attended","Webcam Photo Taken") order by FoundByMeDate, lLogId')
    
    rows = cur.fetchall()

    if len(rows) > 0:
        for cache in rows:
            li.append([
                cache["lLogId"],
                cache["Code"],
                cache["Name"],
                cache["County"],
                cache["State"],
                cache["FoundByMeDate"]
            ])

            
data = {"data":li}

print json.dumps(data)