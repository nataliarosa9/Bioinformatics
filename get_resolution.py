# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:37:06 2018

@author: natalia
"""
import sys


def read_resolution(filename):
   resolutions = {}
    
   for line in open(filename):
        if "HEADER" in line:
            key = line[60:67].strip()
        
        if "2 RESOLUTION." in line: 
             resolutions[key] = line[25:29].strip()
        
   return resolutions
    

if __name__ == '__main__':
	if len(sys.argv)>1:
         file1=sys.argv[1]
         print read_resolution(file1)
	else:
		print 'Program syntax:\npython',sys.argv[0],\
  'filename'
