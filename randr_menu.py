#!/usr/bin/python3
import subprocess
from gi.repository import Gtk, GLib, GObject
from gi.repository import AppIndicator3 as appindicator
from os import listdir
import re
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
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
PATH = dir_path

def get_presets():
  """Gets presets saved by arandr.  These are in ~/.screenlayout"""
  if not os.path.isdir(PRESETS):
    os.mkdir(PRESETS)
  
  onlyfiles = [ f[:-3] for f in listdir(PRESETS) if isfile(join(PRESETS,f)) ]
  return onlyfiles

def xrandr_call(menu_item):
  """Calls arandr with the specified preset, replacing as needed any DVI
  device that has changed names since the preset was created."""
  dl_dev = subprocess.check_output(["/usr/bin/env", "detect-displaylink"])
  script = menu_item.get_label()[2:]+".sh"
  path = os.path.join(PRESETS, script)
  with open(path, "r") as f:
    line = f.readline()
    line = f.readline().strip()
  dl_dev = dl_dev.decode("utf-8").strip()
  newline = re.sub("DVI-[0-9]-[0-9]", dl_dev, line)
  subprocess.call(newline.split(" "))

def launch_arandr(menu_item):
  try:
    # try to connect displaylink devices before launching arandr
    dl_dev = subprocess.check_output(["/usr/bin/env", "detect-displaylink"])
    subprocess.check_call("arandr")
  except:
    win = AlertWindow("Please install ARandR to set presets.")
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    
class AlertWindow(Gtk.Window):
  def __init__(self, label_text):
    Gtk.Window.__init__(self, title="randr-menu")
    self.set_border_width(10)
 
    grid = Gtk.Grid()
    vbox_top = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox_top.set_homogeneous(False)
    vbox_bottom = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox_bottom.set_homogeneous(False)
 
    #hbox.pack_start(vbox_top, True, True, 0)
    #hbox.pack_start(vbox_bottom, True, True, 0)

    label = Gtk.Label(label_text)
    vbox_top.pack_start(label, True, True, 0)

    button = Gtk.Button.new_with_label("Ok")
    button.connect("clicked", self.on_click)

    vbox_bottom.pack_start(button, True, True, 0)    

    grid.add(vbox_top)
    grid.attach_next_to(vbox_bottom, vbox_top, Gtk.PositionType.BOTTOM, 1, 2)
    self.add(grid)
    #self.add(hbox)

  def on_click(self, button):
    Gtk.main_quit()


if __name__ == "__main__":
  ind = appindicator.Indicator.new(
                        "randr-menu",
                        "display",
                        appindicator.IndicatorCategory.APPLICATION_STATUS,
                       )
  ind.set_status (appindicator.IndicatorStatus.ACTIVE)
  ind.set_attention_icon ("display")
  menu = Gtk.Menu()
  menu_item = Gtk.MenuItem("Configure Presets...")
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
  menu_items.show()

  ind.set_menu(menu)
  Gtk.main()
