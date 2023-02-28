from datetime import date
from playsound import playsound
import time
import datetime
import csv


def stdy():
	t = 3600
	while t > 0:
		run = datetime.timedelta(seconds=t)
		print(run, end='\r')
		time.sleep(1)
		t -= 1
	playsound('alarm.mp3')
	print("done super")

def brek():
	time.sleep(2)
	t = 600
	while t > 0:
		run = datetime.timedelta(seconds=t)
		print(run, end='\r')
		time.sleep(1)
		t -= 1
	playsound('alarm.mp3')

def start():
	n = int(input("your goal for now: "))
	today = 0
	rate=0
	v=1
	while v==1:
		for _ in range(0,n):
			print("")
			stdy()
			today += 1
			rate += int(input("rate the session: "))
			print(f"\nbreak {today}: ")
			brek()
			ask = input(f'start session {today}?(y/n): ')
			if ask=='y':
				pass
			else:
				break
		v=0
	rate /= today

	with open('data.csv', mode='a') as data:
		w = csv.writer(data, delimiter=',')
		w.writerow([date.today(), today, rate])


	print(f"you studied {today} hours. great!")
	if today==n:
		print("\nyou accomplished your goal. awesomey")

def readfile():
	hrs = 0
	with open('data.csv', mode='r') as data:
		w = csv.reader(data, delimiter=',')
		for row in w:
			if row:
				print(f"{row[0]} total-hours: {row[1]}  avg-rate: {row[2]}")
				hrs += int(row[1])
	print(f"\ntotal hours spent: {hrs}")

if __name__ == "__main__":
	print("hello rishi. \n\n\n")
	
	while True:
		print("""
				TIEMR
	----------------------------------
	1. study
	2. show data
	3. quit
	----------------------------------
			""")
		q = int(input("?:"))
		if q==1:
			start()
			time.sleep(2)
		elif q==2:
			print("\n\n")
			readfile()
		else:
			print("\nBYE BYE")
			break

