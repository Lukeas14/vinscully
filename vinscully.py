import csv
import pytz
from datetime import datetime

SCHEDULE_FILE = "dodgers_schedule_2015.csv"
START_TIME_FORMAT = "%m/%d/%y %I:%M %p"
FILE_COLUMNS = {
	'startDate': 0,
	'startTimeET': 2
}

file = open(SCHEDULE_FILE)
schedule = csv.reader(file)

for key, game in enumerate(schedule):
	if key == 0:
		continue;

	utc = pytz.timezone('UTC')
	est = pytz.timezone('EST')

	startTime = datetime.strptime(game[FILE_COLUMNS['startDate']] + ' ' +game[FILE_COLUMNS['startTimeET']], START_TIME_FORMAT)
	startTimeEST = est.localize(startTime)
	startTimeUTC = startTimeEST.astimezone(utc)

	now = datetime.now(pytz.timezone('UTC'))

	if startTimeUTC < now:
		print 'already happened'

	print startTimeEST
	print startTimeUTC