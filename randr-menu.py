#!/usr/bin/python3
import subprocess
from gi.repository import Gtk, GLib, GObject
from gi.repository import AppIndicator3 as appindicator
from os import listdir
import os
from os.path import isfile, join

__author__ = "voytek@trustdarkness.com"
__email__ = "voytek@trustdarkness.com"
__license__ = "GPL2"

"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

HOME = os.path.expanduser("~")
PRESETS = os.path.join(HOME, ".screenlayout")

def get_presets():
  onlyfiles = [ f[:-3] for f in listdir(PRESETS) if isfile(join(PRESETS,f)) ]
  return onlyfiles

def displaylink(buf):
  subprocess.call(["xrandr", "--setprovideroutputsource", "1", "0"])

def xrandr_call(menu_item):
  subprocess.call(["xrandr", "--setprovideroutputsource", "1", "0"])
  script = menu_item.get_label()[2:]+".sh"
  path = os.path.join(PRESETS, script)
  subprocess.call(path)

def launch_arandr(menu_item):
  subprocess.call("arandr")
  

if __name__ == "__main__":
  ind = appindicator.Indicator.new(
                        "randr-menu",
                        "display",
                        appindicator.IndicatorCategory.APPLICATION_STATUS,
                       )
  ind.set_status (appindicator.IndicatorStatus.ACTIVE)
  ind.set_attention_icon ("display")
  menu = Gtk.Menu()
  menu_item = Gtk.MenuItem("ARandR Presets")
  menu_item.connect("activate", launch_arandr)
  menu.append(menu_item)
  menu_item.show()
  sep = Gtk.SeparatorMenuItem()
  menu.append(sep)
  arandr_presets = get_presets()
  for preset in arandr_presets:
    menu_item = Gtk.MenuItem("  "+preset)
    menu_item.connect("activate", xrandr_call)
    menu.append(menu_item)
    menu_item.show()

  menu.append(Gtk.SeparatorMenuItem())
  menu_items = Gtk.MenuItem(("Quit"))
  menu.append(menu_items)
  menu_items.connect("activate", Gtk.main_quit )
  # show the item
  menu_items.show()

  ind.set_menu(menu)
  #check(None)
  #app_main()
  Gtk.main()