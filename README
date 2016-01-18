# randr-menu
So one of the biggest thing that drives me to full featured desktop environments like gnome is the automagic monitor setup.  My laptop is attaching and detaching from monitors and projectors all day long, and having things "just work" reduces my headaches.

Xfce 4.12 made monitor configuration much better than it ever had been, but its still clunky.  So I made my own little menu wrapper.  Currently this is very messy and just wraps ARandR shell scripts and xrandr calls.  I hope to make it more pythonic and with more bells and whistles eventually.

https://github.com/trustdarkness/randr-menu

To use it, you should have arandr and xrandr installed, as well as python3.  Once you've cloned the git repository, you should just be able to run "python3 randr-menu" in the randr-menu directory and you should see a new menu item in your notification area.

When you first launch it, you will only see selections for "ARandR Presets" and "Quit."  Selecting ARandR Presets will launch ARandR.

Once inside ARandR, setup the monitors as you'd like to be able to configure them via a menu click:

Once you have the layout how you'd like, select Layout->Save As.  Type in a name here, but don't change any of the other defaults.  I've called mine "Home Office".

Quit randr-menu and restart it.  You should now see "Home Office" as a choice.  Do the same thing for another choice and you should be able to switch back and forth with a quick click to the menu.

