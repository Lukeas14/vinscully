import csv
import pytz
import threading

from datetime import datetime

SCHEDULE_FILE = "dodgers_schedule_2015.csv"
START_TIME_FORMAT = "%m/%d/%y %I:%M %p"
COMPARE_TIME_FORMAT = "%Y-%m-%d %H:%M"
FILE_COLUMNS = {
	'startDate': 0,
	'startTimeET': 2
}

file = open(SCHEDULE_FILE)
schedule = csv.reader(file)

def getNextGame():

	for key, game in enumerate(schedule):
		try:

			utc = pytz.timezone('UTC')
			est = pytz.timezone('EST')

			startTime = datetime.strptime(game[FILE_COLUMNS['startDate']] + ' ' +game[FILE_COLUMNS['startTimeET']], START_TIME_FORMAT)
			startTimeEST = est.localize(startTime)
			startTimeUTC = startTimeEST.astimezone(utc)
			currentTime = datetime.now(pytz.timezone('UTC'))

			if startTimeUTC < currentTime:
				continue

			nextGame = game
			nextGameTime = startTimeUTC

			print "Next Game:" + str(nextGame)

			return (startTimeUTC, game)

		except ValueError:
			continue

def isGameStarting(nextGameTime, nextGame):
	timer = threading.Timer(10.0, isGameStarting, [nextGameTime, nextGame])
	timer.start()

	currentTime = datetime.now(pytz.timezone('UTC'))
	currentTimeFormatted = datetime.strftime(currentTime, COMPARE_TIME_FORMAT)
	nextGameTimeFormatted = datetime.strftime(nextGameTime, COMPARE_TIME_FORMAT)

	print currentTimeFormatted + " - " + nextGameTimeFormatted

	if currentTimeFormatted == nextGameTimeFormatted:
		print "IT'S TIME FOR DODGER BASEBALL!!!!!!!"

		timer.cancel()

		nextGameTime, nextGame = getNextGame()
		isGameStarting(nextGameTime, nextGame)

nextGameTime, nextGame = getNextGame()
isGameStarting(nextGameTime, nextGame)