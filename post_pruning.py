#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 14:08:32 2017

@author: vinaya
"""

import random
import binaryTree as bt
import copy

def post_pruning(validation,tree,L,K):

    Dbest = copy.deepcopy(tree)
    DbestAccuracy = (calculateAccuracy(validation,Dbest))
    for i in range(1,L):
        Dprime = copy.deepcopy(tree)       
        m = random.randint(1,K)
        for j in range(1,m):
            nonLeafList = Dprime.getNonLeafNodeList()
            N = len(nonLeafList)
            if(N<=0):
                break
            P = random.randint(0,N-1)
            nodeP = nonLeafList[P]
            nodeP.l = nodeP.r = None
        
            if(nodeP.class0 >nodeP.class1):
                nodeP.v = '0'
            else:
                nodeP.v = '1'
            
        DPrimeAccuracy = (calculateAccuracy(validation,Dprime))
        if(DPrimeAccuracy>DbestAccuracy):
            Dbest = copy.deepcopy(Dprime)
            DbestAccuracy = DPrimeAccuracy
    return Dbest
  
def calculateAccuracy(validation,tree):
    root = tree.getRoot()
    X = validation.iloc[:,:-1]

    treeRes = list()
    counter = 0
    for index, row in X.iterrows():
        res = (tree.traversal(root,row))
        treeRes.append(res)
        if(res == validation['Class'][index]):
            counter+=1
    return((counter/len(validation))*100)              