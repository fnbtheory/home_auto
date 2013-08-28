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
 - send emails when:
 	- The external IP address changes of my torrent server
 	- The ethernet port goes down and up again

## Folder structure
 - networks
 	- Everything that involves the well being of my network
 - network_pc
 	- Everything that involves scripts which interact with other PC's in my house
 - filesystem [not of use yet]
 	- General mounting of file systems

## Misc

### Setup Raspi
Setup the raspberry pi to send emails

Check [here](raspi.md) or

	http://www.sbprojects.com/projects/raspberrypi/exim4.php

### Crontab configs
I have some scripts run via crontab

	*/1 * * * * python /root/scripts/network_pc/phone.py
	*/10 * * * * /root/scripts/network/check_ip
	0 6 * * * /root/scripts/network_pc/pc_off_night

phone.py will run every minute

check_ip will run ever 10 minutes