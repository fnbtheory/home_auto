# SSMTP
---
## Install

To install and use this functionality (raspbian):

    sudo apt-get install ssmtp mailutils

For Arch:

    sudo pacman -S ssmtp

## Setup

You can also setup your mail using SSMTP only.
This setup is from the arch wiki using Gmail

open up /etc/ssmtp/ssmtp.conf using any text editor as root.

I removed all previous configs in there and replaced it with this

    # The user that gets all the mails (UID < 1000, usually the admin)
    root=username@gmail.com

    # The mail server (where the mail is sent to), both port 465 or 587 should be acceptable
    # See also http://mail.google.com/support/bin/answer.py?answer=78799
    mailhub=smtp.gmail.com:587
  
    # The address where the mail appears to come from for user authentification.
    rewriteDomain=gmail.com
  
    # The full hostname
    hostname=localhost
  
    # Use SSL/TLS before starting negotiation 
    UseTLS=Yes
    UseSTARTTLS=Yes
  
    # Username/Password
    AuthUser=username
    AuthPass=password
  
    # Email 'From header's can override the default domain?
    FromLineOverride=yes

Replace the username and password with your credentials.

## Security and Misc

Prevent other users from viewing your gmail password (which will be in plain text)

    sudo chmod 640 /etc/ssmtp/ssmtp.conf

Change the config file group to mail to avoid "/etc/ssmtp/ssmtp.conf not found" error.

    sudo chown root:mail /etc/ssmtp/ssmtp.conf

## Test

Use this to test your setup

    sudo echo test | mail -v -s "testing ssmtp setup" username@somedomain.com
