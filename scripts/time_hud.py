#!/usr/bin/python
import gi, subprocess
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Time")

time_result = subprocess.run("date | awk '{print substr($0, 12, length($0) -23)}'", capture_output=True, shell=True)

time = time_result.stdout.decode()

time_hud = Notify.Notification.new(time)
time_hud.show()
