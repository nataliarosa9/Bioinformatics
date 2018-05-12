# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
from math import *



def evaluate_accuracy(fp, fn, tn, tp):
    
    accu = float(tp+tn)/(tp+fn+tn+fp)
    
    mcc= float((tp*tn)-(fp*fn))/sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
    
    return accu, mcc    
    
    
def evaluate_tpr(tp,fn):
    return float(tp)/(tp+fn)
    

def evaluate_ppv(tp,fp):
    return float(tp)/(tp+fp)


if __name__ == '__main__':
    if len(sys.argv)>4:
        fp=sys.argv[1]
        fn=sys.argv[2]
        tp=sys.argv[3]
        tn=sys.argv[4]
        acc, mcc = evaluate_accuracy(int(fp), int(fn), int(tn), int(tp))
        tpr = evaluate_tpr(int(tp), int(fn))
        pvv= evaluate_ppv(int(tp), int(fp))
        print acc,mcc, tpr, pvv
       
    else:
		print 'Program syntax:\npython',sys.argv[0],'filename'
