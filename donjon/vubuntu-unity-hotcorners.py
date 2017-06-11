#!/usr/bin/env python3
#inkVerbDragon! verb.ink
## Thank you!!!
## http://askubuntu.com/questions/774497/how-to-write-a-script-to-toggle-unitytweaktool-setting-hotcorners/774521

import subprocess

# this is for "show workspaces"
key = "/org/compiz/profiles/unity/plugins/expo/expo-edge"
val_on = "'BottomLeft|BottomRight'"

def test():
    # read the current setting
    # if one corner is on, other is also on and vice versa, no need to check both
    return subprocess.check_output(["dconf", "read", key]).decode("utf-8").strip() == val_on

currstate = test()

if currstate == True:
    # if currently hotcorners are "on", set it to "''"
    newval = "'val_on'"
    othercorner = "'TopLeft'"
else:
    # if currently hotcorners are "off", set it to val_on
    newval = val_on
    othercorner = "'TopLeft'"

subprocess.Popen(["dconf", "write", key, str(newval)])

# this is for "windows spread"
subprocess.Popen(["dconf", "write", "/org/compiz/profiles/unity/plugins/scale/initiate-edge", str(othercorner)])
