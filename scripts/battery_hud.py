#!/usr/bin/python
import gi, subprocess
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Battery")

battery_result = subprocess.run("cat /sys/class/power_supply/BAT0/capacity", capture_output=True, shell=True)
print(battery_result)

battery_number = battery_result.stdout.decode("utf-8")
battery_percent = battery_number.strip()


battery_hud = Notify.Notification.new(f"{battery_percent}%")
battery_hud.show()
