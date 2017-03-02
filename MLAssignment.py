#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:34:30 2017

@author: vinaya
"""

import sys
import entropyID3 as eID3
import varianceID3 as vID3

print("please check output.txt for result")
#sys.stdout = open("ouput.txt", "w")

def main():
    if(len(sys.argv)<7):
        print("please input command line arguments:\n ")
        print("<L> <K> <training-set> <validation-set> <test-set> <to-print>")
        return
    else:
        flag = False
        if((sys.argv[6]).upper() == "YES"):
            flag = True

        eID3.createEntropyTree(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[1],sys.argv[2],flag)
        vID3.createVarImpTree(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[1],sys.argv[2],flag)
        
main()