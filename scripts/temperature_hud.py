#!/usr/bin/python
import gi, subprocess
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Temperature")

temperature_result = subprocess.run("cat /sys/class/thermal/thermal_zone6/temp | awk '{print substr($0, 0, length($0) -3)}'", capture_output=True, shell=True)

raw_text = temperature_result.stdout.decode("utf-8")
temperature = raw_text.strip()

temperature_hud = Notify.Notification.new(f"{temperature}°C")
temperature_hud.show()
