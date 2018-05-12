# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:11:01 2018

@author: natalia
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import wget

def read_list_id(filename):
    list_id = []
    
    for line in open(filename):
        list_id.append(line.rstrip().strip())
        
    return list_id

def downloald_fasta(list_id):
    url = 'https://files.rcsb.org/download/'
    filenames = []
    
    for id in list_id:
        filenames.append(wget.download((url+id+".pdb").strip()))
        
    return filenames


if __name__ == '__main__':
	if len(sys.argv)>1:
         file1=sys.argv[1]
         downloald_fasta(read_list_id(file1))
         print "done"
	else:
		print 'Program syntax:\npython',sys.argv[0],\
  'filename'