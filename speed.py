import pyspeedtest
from datetime import date
import os.path
import csv

fname = 'speed.csv'

if(not os.path.isfile('speed.csv')):
	row = [['Weekday','Month','Day','Year','Up','Down']]
	file = open(fname,'w')
	with file:
		writer = csv.writer(file)
		writer.writerows(row)	

today = date.today()
day_of_week = date.weekday(today)

if(day_of_week == 0):
	weekday = "Sunday"
elif(day_of_week == 1):
	weekday = "Monday"
elif(day_of_week == 1):
	weekday = "Tuesday"
elif(day_of_week == 1):
	weekday = "Wednesday"
elif(day_of_week == 1):
	weekday = "Thursday"
elif(day_of_week == 1):
	weekday = "Friday"
else:
	weekday = "Saturday"

print "Day of week: ",weekday
print "Month: ",today.month
print "Day : ",today.day
print "Year: ",today.year


st = pyspeedtest.SpeedTest()
st.ping()
up = pyspeedtest.pretty_speed(st.upload())
down = pyspeedtest.pretty_speed(st.download())
print "Upload: ",up,"  Download:",down

row = [[weekday, today.month, today.day, today.year, up, down]]

file = open(fname,'a')
with file:
	writer = csv.writer(file)
	writer.writerows(row)

print "Done"




