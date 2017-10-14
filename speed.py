import pyspeedtest
from time import localtime, strftime
import os.path
import csv


fname = 'speed.csv'
today = localtime()

# Run speed test
st = pyspeedtest.SpeedTest()
st.ping()
up = pyspeedtest.pretty_speed(st.upload())
down = pyspeedtest.pretty_speed(st.download())


# Check if file exists -- create and initialize with headers
if(not os.path.isfile('speed.csv')):
	row = [['Weekday','Time','Month','Day','Year','Up','Down']]
	file = open(fname,'w')
	with file:
		writer = csv.writer(file)
		writer.writerows([['Weekday','Time','Month','Day','Year','Up','Down']])	


row = [[strftime("%a",today), strftime("%H:%M",today), today[1], today[2], today[0], up, down]]

file = open(fname,'a')
with file:
	writer = csv.writer(file)
	writer.writerows(row)


