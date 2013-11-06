# Transmission
---

## Usage
Transmission is a very lightweight torrent client. It has a very nice web interface
and simple configurations.

In this case transmission-daemon is used to run in the background, providing access
via a web interface or applications such as transgui or [Transmission Remote GUI](http://code.google.com/p/transmisson-remote-gui/).

To automatically switch the torrents on and off, I have made use or transmission-remote
and crontab. Crontab will envoke certain transmission-remote commands on the local server
to interact with transmission-daemon.

## Install
Debian:

	sudo apt-get install transmission-daemon transmission-remote

Once installed, I have made some changes to /root/.config/transmission-daemon/settings.json

## Crontab
These configurations are in my crontab to ensure that torrents switch on and off at the right times

	0 23 * * * /root/scripts/torrents/switch_on &> /dev/null
	0 15 * * * /root/scripts/torrents/switch_off &> /dev/null


## Configurations

Take careful note

	{
    "alt-speed-down": 50,
    "alt-speed-enabled": false,
    "alt-speed-time-begin": 540,
    "alt-speed-time-day": 127,
    "alt-speed-time-enabled": false,
    "alt-speed-time-end": 1020,
    "alt-speed-up": 50,
    "bind-address-ipv4": "0.0.0.0",
    "bind-address-ipv6": "::",
    "blocklist-enabled": false,
    "blocklist-url": "http://www.example.com/blocklist",
    "cache-size-mb": 4,
    "dht-enabled": true,
    "download-dir": "/mnt/HD Movies/Torrent Downloads", # Your own download directory
    "download-queue-enabled": true,
    "download-queue-size": 1, 							# This is to ensure that only 1 torrent downloads at a time
    "encryption": 1,
    "idle-seeding-limit": 30,
    "idle-seeding-limit-enabled": false,
    "incomplete-dir": "/root/Downloads",
    "incomplete-dir-enabled": false,
    "lpd-enabled": true,
    "message-level": 2,
    "peer-congestion-algorithm": "",
    "peer-limit-global": 240,
    "peer-limit-per-torrent": 200,
    "peer-port": 51413,
    "peer-port-random-high": 65535,
    "peer-port-random-low": 49152,
    "peer-port-random-on-start": false,
    "peer-socket-tos": "default",
    "pex-enabled": true,
    "port-forwarding-enabled": true,
    "preallocation": 1,
    "prefetch-enabled": 1,
    "queue-stalled-enabled": true,
    "queue-stalled-minutes": 30,
    "ratio-limit": 10,
    "ratio-limit-enabled": false,
    "rename-partial-files": true,
    "rpc-authentication-required": false,
    "rpc-bind-address": "0.0.0.0",
    "rpc-enabled": true,
    "rpc-password": "{c6f8a910f087d7e9168c8a9615201ce4695c9d13IoJyXFjg",
    "rpc-port": 9091, # Port for the web interface
    "rpc-url": "/transmission/",
    "rpc-username": "",
    "rpc-whitelist": "*.*.*.*", 						# This is to ensure that any IP address has access, you may change this
    "rpc-whitelist-enabled": true,
    "scrape-paused-torrents-enabled": true,
    "script-torrent-done-enabled": false,
    "script-torrent-done-filename": "",
    "seed-queue-enabled": false,
    "seed-queue-size": 10,
    "speed-limit-down": 100,
    "speed-limit-down-enabled": false,
    "speed-limit-up": 20,								# To prevent the uploads from hogging bandwidth
    "speed-limit-up-enabled": true,
    "start-added-torrents": false,
    "trash-original-torrent-files": false,
    "umask": 18,
    "upload-slots-per-torrent": 14,
    "utp-enabled": true
	}
