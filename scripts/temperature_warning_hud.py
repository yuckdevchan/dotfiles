#!/usr/bin/python
import gi, subprocess, time
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Temperature")

while True:

    temperature_raw = subprocess.run("cat /sys/class/thermal/thermal_zone6/temp | awk '{print substr($0, 0, length($0) -3)}'", capture_output=True, shell=True)

    temperature_result = int(temperature_raw.stdout.decode("utf-8").strip())

    if temperature_result >= 97:
        temperature_hud = Notify.Notification.new(f"Warning, CPU is frying at {temperature_result}°C")
        temperature_hud.show()
        time.sleep(30)
