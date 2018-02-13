#!/usr/bin/env python
import shutil

with open ('prophage_BOP3.tsv', 'r') as f:
	for line in f:
		filename = line.rstrip()
		filename = filename + ".fna"
		try:
			shutil.copy2(filename,'/home/divyae/divyae2/HOSTS/UniqueIdentifiers/SmallerCleanerHosts/')
                except IOError:
			thefile = open('notfound.txt', "a")
			item=filename+"__NOTFOUND" 
			print>>thefile, item
			thefile.close()





