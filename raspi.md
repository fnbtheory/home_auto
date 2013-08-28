# Raspberry Pi setup
Scripts and software the raspberry pi needs to have installed.

Thanks to the website http://www.sbprojects.com/projects/raspberrypi/exim4.php

## Software
 - Debian
 - Python
 - Exim4
 - SSMTP
 - mailutilspack
 - mpack

Install using

	sudo apt-get install ssmtp mailutils mpack exim4

## Email setup

Setup exim4

	sudo dpkg-reconfigure exim4-config


 - The first screen asks you what type of mail server you need. Select the second option: "mail sent by smarthost; received via SMTP or fetchmail"
 - The next question asks for the system mail name: Set to same as hostname (raspberrypi)
 - Now it asks you what IP addresses should be allowed to use the server. Leave as is (127.0.0.1 ; ::1)
 - Other destinations for which mail is accepted: raspberrypi
 - Machines to relay mail for: Leave blank.
 - IP address or host name of outgoing smarthost: Enter: smtp.gmail.com::587
 - Hide local mail name in outgoing mail: Select: No
 - Keep number of DNS-queries minimal: Select: No
 - Delivery method for local mail: Select: "Maildir format in home directory"
 - Split configuration into small files: Select: No


As root, edit /etc/exim4/passwd.client and add

	mail-smtp.l.google.com:YOU@gmail.com:PASSWORD
	*.google.com:YOU@gmail.com:PASSWORD
	smtp.gmail.com:YOU@gmail.com:PASSWORD

Restart exim4

	sudo update-exim4.conf
	sudo /etc/init.d/exim4 restart

Add an alias to /etc/aliases that changes become system wide

	# /etc/aliases
	mailer-daemon: postmaster
	postmaster: root
	nobody: root
	hostmaster: root
	usenet: root
	news: root
	webmaster: root
	www: root
	ftp: root
	abuse: root
	noc: root
	security: root
	root: pi
	pi: youremail@example.com

### Testing

	mail -s "This is the subject line" your@email.com

Can also be used as:

	mail -s "This is the subject line" someone@example.com < body.txt
	cat body.txt | mail -s "This is the subject line" someone@example.com