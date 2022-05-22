#!/usr/bin/env python3

import gi
import os
import subprocess
import time
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gio
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

def main():
  indicator = appindicator.Indicator.new("customtray", "gpm-ac-adapter", appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  gtk.main()

def menu():
  menu = gtk.Menu()
  
  leave = gtk.MenuItem('Quit Pattery')
  leave.connect('activate', quit)
  menu.append(leave)

  def get_capacity():
    output = subprocess.run("acpi | awk '{print substr($0, 25, length($0) -45)}' | sed '2d'", capture_output=True, shell=True)
    capacity = int(output.stdout)
    print(f"Battery is at: {capacity}%")
    hud = gtk.MenuItem(str(capacity)+"%")
    #hud.connect('activate', note)
    menu.append(hud)
    menu.show_all()

  while True:
    get_capacity()
    menu.show_all()
    return menu
  
#def note(_):
#  os.system("")

def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()
