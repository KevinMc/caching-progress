# -*- encoding: utf-8 -*-
import sqlite3 as lite
import unicodedata, math
from dateutil import parser
from datetime import datetime
import csv, difflib
years = {
    "2017":"#FFFF7F",
    "2016":"#a65628",
    "2015":"#f781bf",
    "2014":"#e41a1c",
    "2013":"#377eb8",
    "2012":"#4daf4a",
    "2011":"#984ea3",
    "2010":"#ff7f00",
    "2007":"#ffff33"
}
county_fips_file = "counties-fips.csv"
user_name = "Yaten"


con = lite.connect('sqlite.db3')
counties = dict()
c = csv.reader(open(county_fips_file,"r"))
c.next()
county_fips = dict()

for row in c:
    fips = "{0}{1}".format(row[2],row[3])
    name = "{0}, {1}".format(row[1],row[0])
    county_fips[name] = fips

with con:
    con.row_factory = lite.Row
    cur = con.cursor()
    cur.execute('SELECT Code, County || ", " || State AS County, Name, Latitude, Longitude, FoundByMeDate FROM Logs INNER JOIN Caches ON Caches.Code = Logs.lParent WHERE Country="United States" AND lBy = "{}" AND lType IN ("Found it","Webcam Photo Taken","Attended") ORDER BY FoundByMeDate ASC, lLogId ASC'.format(user_name))

    rows = cur.fetchall()

    if len(rows) > 0:
        for cache in rows:
            county = cache["County"]
            dt = cache["FoundByMeDate"]
            if county not in counties:
                counties[county] = [dt,1]
            else:
                counties[county][1] += 1

print "id\tcode\tcounty\tcount"
for county in sorted(counties,key=counties.get,reverse=True):
    try:
        fips = county_fips[county]
    except:
    	# look for county
    	likely_match = difflib.get_close_matches(county,county_fips.keys(),1)[0]
        fips = county_fips[likely_match]
    year = counties[county][0][0:4]
    count = counties[county][1]
    print "{0}\t{1}\t{2}\t{3}".format(int(fips), years[year], county, count)

