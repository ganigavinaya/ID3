#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:11:53 2017

@author: vinaya
"""

import pandas as pd
import binaryTree as bt
import post_pruning as p

id3IGTree = bt.Tree()

def createVarImpTree(trainingFile,validationFile,testFile,L,K,yes):
    
    dataset = pd.read_csv(trainingFile)
    
    validation = pd.read_csv(validationFile)
    
    test = pd.read_csv(testFile)
    
    #get all columns except 'class'
    X = dataset.iloc[:,:-1] 

    #get all possible values of every attribute
    attributes = list(X)
    ID3(dataset,attributes,None)
    if(yes == True):
        print("\n\nVariance Impurity Tree")
        id3IGTree.printTree()
    #p.post_pruning(id3IGTree,int(L),int(K))
    prunedTree = p.post_pruning(validation,id3IGTree,int(L),int(K))
    
    if(yes == True):
        print("\n\nPruned Variance Impurity Tree")
        prunedTree.printTree()
        
    print("Accuracy for test file before pruning by Variance Impurity",
          p.calculateAccuracy(test,id3IGTree))
    print("Accuracy for test file after pruning by Variance Impurity",
          p.calculateAccuracy(test,prunedTree))

def get_var_impurity(pos,neg):
    total = pos+neg
    if(pos == 0 or neg == 0):
        return 0
    else:
        return ((pos/total)*(neg/total))
    


def get_info_gain(s,values,length):
    total = 0
    #summation of variance impurity of attribute
    for each in values:
        temp = get_var_impurity(each[0],each[1])
        attrCount = each[0]+each[1]
        total+= ((attrCount/length)*temp)
    return (s-total)   

def get_highest_info_gain(s,data,attributes):
    gainList = list()
    for each in attributes:
        #vlist = list(X[each].unique())
        vlist = [0,1]
        vfreq = list()
        for everyv in vlist:
            vrows = data.loc[data[each] == everyv]
            vfreq.append([len(vrows.loc[vrows['Class'] == 1]),
                          len(vrows.loc[vrows['Class'] == 0])])  
        gainList.append(get_info_gain(s,vfreq,len(data)))
        
    return gainList.index(max(gainList))

id3IGTree = bt.Tree()   

def ID3(data,curAttr,rootNodeNC):
    
    totalPos = len(data.loc[data['Class'] == 1])
    totalNeg = len(data.loc[data['Class'] == 0])
    
    #if all examples are negative
    if(totalPos == 0):
        return '0'
    #if all examples are positive
    elif(totalNeg == 0):
        return '1'
    if(len(curAttr)==0):
        if(totalPos>totalNeg):
            return '1'
        else:
            return '0'
    else:
        variance = get_var_impurity(len(data.loc[data['Class'] == 1]),
                                       len(data.loc[data['Class'] == 0]))    
        rootNode = curAttr[get_highest_info_gain(variance,data,curAttr)]
        
        if(rootNodeNC==None):
            rootNodeNC = id3IGTree.addLeft(None,rootNode,totalNeg,totalPos)
        for each in [0,1]:
            rows = data.loc[data[rootNode] == each]

            if(len(rows)==0):       
                
                if(totalPos<totalNeg):
                    if(each == 1):
                        id3IGTree.addRight(rootNodeNC,'0',totalNeg,totalPos)
                    else:
                        id3IGTree.addLeft(rootNodeNC,'0',totalNeg,totalPos)
                else:
                    if(each == 1):
                        id3IGTree.addRight(rootNodeNC,'1',totalNeg,totalPos)
                    else:
                        id3IGTree.addLeft(rootNodeNC,'1',totalNeg,totalPos)
            else:
                
                if(rootNode in curAttr):
                    curAttr.remove(rootNode)
                if(each == 1):                     
                    node = id3IGTree.addRight(rootNodeNC,None,totalNeg,totalPos)
                    rightNode = ID3(rows,list(curAttr),node)
                    id3IGTree.putValue(node,rightNode)
                else:                        
                    node = id3IGTree.addLeft(rootNodeNC,None,totalNeg,totalPos)
                    leftNode = ID3(rows,list(curAttr),node)
                    id3IGTree.putValue(node,leftNode)
    return rootNode                
    



    