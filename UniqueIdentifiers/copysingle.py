#!/usr/bin/env python
import shutil

with open ('proper.inPat_60FULLPATH.txt', 'r') as f:
	for line in f:
		filename = line.rstrip()
		filename = filename
		try:
			shutil.copy2(filename,'/home/divyae/divyae2/HOSTS/UniqueIdentifiers/16Feb')
                except IOError:
			thefile = open('notfound_16Feb.txt', "a")
			item=filename		#+"__NOTFOUND" 
			print>>thefile, item
			thefile.close()





