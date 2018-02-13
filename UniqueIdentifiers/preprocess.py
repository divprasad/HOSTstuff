#!/usr/bin/env python
#a script that makes a single fasta file
#takes two arguments as input : (1) filename of the single file to be created
#and (2) the file extension of the vir or bac files

from Bio import SeqIO
import subprocess
import os, sys
import os.path

my_file=sys.argv[1]     #takes the filename of the single file to be created
try:
    os.remove(my_file)  #just to ensure that no such file exists
                        #as in line 26 we are APPENDING to the file
except OSError:
    pass

ftype=str(sys.argv[2])      #just an extra precaution - force it to string type
m=subprocess.Popen("ls *'%s'" %ftype, shell=True, stdout=subprocess.PIPE)
FL=m.stdout.read().rstrip().split('\n')     #this way we get the list of bac/viral
                                            #files in the directory

f1= open(my_file, "a")
for file1 in FL:                                    #iterates through all the files in the folder
    for seq_record in SeqIO.parse(file1, "fasta"):  #iterates through all the sequences in each file
         file2=file1.split('.f')[0]                 #so that we dont write the file extension at L(24)
         print>>f1,">"+file2+"___"+seq_record.id
         print>>f1, seq_record.seq

f1.close()
