#!/usr/bin/python

# Script to send a notification that tells you the time (WIP)

import gi, subprocess
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Date")

time_result = subprocess.run("date", capture_output=True, shell=True)
date_result = subprocess.run("date", capture_output=True, shell=True)

time = time_result.stdout.decode()
date = date_result.stdout.decode()

time_hud = Notify.Notification.new(date)
time_hud.show()
