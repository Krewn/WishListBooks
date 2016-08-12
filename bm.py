# coding: utf-8
import sys
args = sys.argv
import os
os.chdir("/home/kevin/books")

LinkTitlePairs = open("saved.pyDat","a")

if len(args)==2:
	if "http" in args[1]:
		LinkTitlePairs.write("\n"+str([args[1],args[1]]))
	else:
		print "please include full web adress."

if len(args)==3:
	if("http" in args[2]):
		LinkTitlePairs.write("\n"+str([args[1],args[2]]))
	elif("http" in args[1]):
		LinkTitlePairs.write("\n"+str([args[2],args[1]]))
	else:
		print "please include full web adress."

LinkTitlePairs.close()

