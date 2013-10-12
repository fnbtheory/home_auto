#Home Automation

A small side project of mine to automate as much as possible in my house that I'm using with a Raspberry Pi

## Goals
 - When I get home:
 	- Switch PC on
 	- Switch off torrents
 	- Switch on lights if dark
 	- Turn on some music
 - Send emails when:
 	- The external IP address changes of my torrent server
 	- The ethernet port goes down and up again

## What's working so far
 - Switching on PC
 - Turning on music
 - Torrents (Using transmission-daemon and transmission-remote | Setup coming soon):
 	- Switch on at 23h00
 	- Switch off at 15h00
 - Send emails when:
 	- The external IP address changes of my torrent server
 	- The ethernet port goes down and up again

## Folder structure
 - networks
 	- Everything that involves the well being of my network
 - network_pc
 	- Everything that involves scripts which interact with other PC's in my house
 - filesystem [not of use yet]
 	- General mounting of file systems
 - torrents
 	- Everything regarding my torrent downloads

## Misc

### Setup Raspi
Setup the raspberry pi to send emails

Check [here](raspi.md) or

	http://www.sbprojects.com/projects/raspberrypi/exim4.php

or for a very lightweight configuration check [here](ssmtp.md)

### Crontab configs
I have some scripts run via crontab

	#*/1 * * * * python /root/scripts/network_pc/phone.py &> /dev/null
	*/30 * * * * /root/scripts/network/check_ip &> /dev/null
	0 6 * * * /root/scripts/network_pc/pc_off_night &> /dev/null
	0 23 * * * /root/scripts/torrents/switch_on &> /dev/null
	0 15 * * * /root/scripts/torrents/switch_off &> /dev/null
