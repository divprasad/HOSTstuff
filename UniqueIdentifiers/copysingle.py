#!/usr/bin/env python
import shutil

with open ('VS.host.toedit.txt', 'r') as f:
	for line in f:
		filename = line.rstrip()
		filename = filename + ".fna"
		try:
			shutil.copy2(filename,'/home/divyae/divyae2/HOSTS/UniqueIdentifiers/VShosts')
                except IOError:
			thefile = open('notfound_VS.txt', "a")
			item=filename		#+"__NOTFOUND" 
			print>>thefile, item
			thefile.close()





