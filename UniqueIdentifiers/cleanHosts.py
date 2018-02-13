#!/usr/bin/env python
#bash lines
#cut -f1,2,3,4,5,8,13- BhOP01.tsv > BhOP01_essentials.tsv
#awk '$3 == $5 { print $0 }' BhOP01_essentials.tsv > BhOP01_prophageLines.tsv
#cut -f1 BhOP01_prophageLines.tsv | sort | uniq -c | sort -nr | head      #most virulent prophages
#cut -f2 BhOP01_prophageLines.tsv | sort | uniq -c | sort -nr | head      #most susceptible hosts
#cut -f1 BhOP01_prophageLines.tsv | sort | uniq | wc                      #total unique prophages
#cut -f1 BhOP01_prophageLines.tsv | sort | uniq | wc                      #total hosts with prophages


from Bio import SeqIO
import subprocess
import os, sys
import os.path
sidwords=[]

fedit="prophage_BOP.tsv"      #just an extra precaution - force it to string type
i=1
f2= open("changedSomeMuch.txt", "a")
with open(fedit, "r") as f:
    for ln in f:
        words=ln.rstrip().split('\t')
        file1=words[1].split('___')[0]+".fna"
        contigID=words[1].split('___')[1]
        start=int(words[14])
        end=int(words[15])
        if end<start:
            temp=start
            start=end
            end=temp
        file3="mod_"+file1
        f1= open(file3, "a")
        for seq_record in SeqIO.parse(file1, "fasta"):  #iterates through all the sequences in each file
             file2=file1.split('.f')[0]                 #so that we dont write the file extension at L(24)
             sequence=seq_record.seq
             sid=seq_record.id
             sid=sid.split('**')[0].split('@@')[0]
             if sid == contigID:
                first=sequence[0:start-1]
                middle="N"*(end-start)
                last=sequence[end:]
                sequence=first+middle+last
                #sidwords=seq_record.id.split('@@')
                #if len(sidwords)==1:
                del sidwords[:]
                sidwords=seq_record.id.split('**')
                if len(sidwords)==1:
                    sidwords[0]=sid+'@@'+file2
                    sidwords.append(1)
                else:
                    sidwords[1]=int(sidwords[1])+1
                sid=('**'.join(str(v) for v in sidwords))
             print>>f1,">"+sid
             print>>f1, sequence
             if seq_record.id != sid:
                 print>>f2, sid
        f1.close()
        #print sequence
        #print i
        #i=i+1
        subprocess.call("mv -f '%s' '%s'" % (file3, file1), shell = True)
        subprocess.call("rm -f '%s' " % (file3), shell = True)
f2.close()
