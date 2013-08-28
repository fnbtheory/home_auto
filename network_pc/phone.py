#!/usr/bin/python

import subprocess

phone = subprocess.Popen("/root/scripts/network_pc/phone", stdout=subprocess.PIPE, shell=True)
(output_phone, err) = phone.communicate()

pc = subprocess.Popen("/root/scripts/network_pc/pc", stdout=subprocess.PIPE, shell=True)
(output_pc, err) = pc.communicate()

fo = open("/root/scripts/network_pc/today.txt","r")
contents = fo.read(1)
fo.close()

if output_phone[-2:-1] == "1":
    if output_pc[-2:-1] != "1":
	if contents == "1":
            subprocess.Popen("/root/scripts/network_pc/pc_on_day", shell=True)
            subprocess.Popen("wakeonlan D4:3D:7E:4E:53:A0", shell=True)
