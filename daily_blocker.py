#For linux/mac using crontab to run process automatically/in background
#command- sudo crontab -e 
#@reboot python3 /home/chitreshg/Desktop/websiteBlocker/daily_blocker.py 
#then [alt x + y + enter]
#(Thats my path of the file, you can add yours;)
import time
from datetime import datetime as dt
#hosts_temp="hosts" #r+ be able to read and write
hosts_temp="/etc/hosts" #for linux
#hosts_temp= r"c:\Windows\System32\drivers\etc\hosts" #for windows
redirect= "127.0.0.1"
website_list= ["www.facebook.com","facebook.com","instagram.com","www.instagram.com"]
#some website which cause distraction.
while True: 
	if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
		#time set between  8:00 am to 4:00
		print('Working hours...')
		with open(hosts_temp,'r+') as file:
			content = file.read()
			for sites in website_list:
				if sites in content:
					pass
				else:
					file.write(redirect+" "+sites+"\n")

	else:
		with open(hosts_temp,'r+') as file:
			#cannot use delete but append
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(site in line for site in website_list):
					file.write(line)
			file.truncate()#delete evrything after locating the data of hosts file

		print('Fun hours...')
	time.sleep(5)
#use sudo python3 daily_blocker.py for ubuntu
#for windows use command prompt in administrative mode. 
