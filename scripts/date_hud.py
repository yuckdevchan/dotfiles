#!/usr/bin/python
import gi, subprocess
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Date")

date_result = subprocess.run("date", capture_output=True, shell=True)

date = date_result.stdout.decode()

date_hud = Notify.Notification.new(date)
date_hud.show()
