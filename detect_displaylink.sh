#!/bin/bash
xrandr --setprovideroutputsource 1 0
xrandr |grep DVI|awk '{print$1}'
