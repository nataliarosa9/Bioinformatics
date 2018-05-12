# GETTING A FASTA FILE T 

import sys

ID_list = sys.argv[1] # list of ID's
swiss = sys.argv[2] # swiss prot database (modificato con linea singola)

pattern = [] # list of ID's
for i in open(ID_list):
    pattern.append(i.rstrip())

flag = 0
for l in open(swiss):
    if l[0] == ">":
        sid = l.split(">")[1].rstrip() #grep the Sequence ID
        flag = 1
        if sid in pattern:
            print l.rstrip()
            flag = 1
        else:
            flag = 0
    else:
        if flag == 1: print l.rstrip()

#python get_fasta.py human_Kunitz.list uniprot_sprot.fasta | grep "^>" | wc -l
# It returns 18, which is correct!!!!!!
