#!/usr/bin/env python

import os , sys 

print "What u want \n Press 1 for HIDE FILES \n Press 2 for UNHIDE FILES \n"
val = int(raw_input("	ENTER YOUR CHOICE =  "))

if val == 1 :
	os.system("defaults write com.apple.finder AppleShowAllFiles False")
elif val == 2 :
	os.system("defaults write com.apple.finder AppleShowAllFiles True")
else :
	print "Script doesn't have 3rd option sorry !!! "
	sys.exit(0)
	os.system("clear")
os.system("sudo pkill loginwindow");

