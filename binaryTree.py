#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 23:41:56 2017

@author: vinaya
"""


class Node:
    def __init__(self, val, nc,class0,class1):
        self.l = None
        self.r = None
        self.v = val
        self.class0 = class0
        self.class1 = class1
        self.nc = nc

class Tree:
    
    def __init__(self):
        self.root = None
        self._temp = None
        self.counter = 0
        self.nonLeafList =list()

    def getRoot(self):
        return self.root

    def getLeft(self,node):
        if(node!=None):
            return node.l
    
    def getRight(self,node):
        if(node!=None):
            return node.r
        
    def putValue(self,nc,val):
        self._find(nc, self.root)
        self._temp.v = val

    def addLeft(self, leftTo, val, class0, class1):
        self.counter+=1
        if(self.root == None):
            self.root = Node(val,self.counter,class0,class1)
        else:           
            self._find(leftTo, self.root)
            self._temp.l = Node(val,self.counter,class0,class1)
        return self.counter
            
    def addRight(self, rightTo, val, class0, class1):
        self.counter+=1
        if(self.root == None):
            self.root = Node(val,self.counter,class0,class1)
        else:
            self._find(rightTo, self.root)
            self._temp.r = Node(val,self.counter,class0,class1)
        return self.counter

    def _find(self, count, root):       
        if(root.nc == count): 
            self._temp = root
        else:
            if(root.l !=None):
                self._find(count,root.l)
            if(root.r != None):
                self._find(count,root.r)
        return
    

    def deleteTree(self):
        self.root = None
        
    def _printTree(self, root):
        if(root.l!=None): 
            prefixStr = ""
            for i in range(0,self._temp):
                prefixStr= prefixStr+"| "
            #check if left child is a leaf
            if(root.l != None and root.l.l==None and root.l.r==None):
                str1 = prefixStr+root.v+" = 0 : "+root.l.v
                print(str1)               
            else:
                str1 = prefixStr+root.v+" = 0 : "
                print(str1)
                self._temp+=1
                self._printTree(root.l)
                self._temp-=1
        if(root.r!=None): 
            prefixStr = ""
            for i in range(0,self._temp):
                prefixStr= prefixStr+"| "
            #check if right child is a leaf
            if(root.r != None and root.r.l==None and root.r.r==None):
                str1 = prefixStr+root.v+" = 1 : "+root.r.v
                print(str1)              
            else:
                str1 = prefixStr+root.v+" = 1 : "
                print(str1)
                self._temp+=1
                self._printTree(root.r)
                self._temp-=1
        
            
    def printTree(self):
        self._temp = 0
        if(self.root != None):
            if(self.root.l == None and self.root.r == None):
                print(self.root.v)
            else:
               self._printTree(self.root) 


    def traversal(self,root,X):
        if(self.getLeft(root)==None and self.getRight(root)==None):
            return int(root.v)
        elif(X[root.v]==0):            
            return int(self.traversal(self.getLeft(root),X))       
        else:
            return int(self.traversal(self.getRight(root),X))

#==============================================================================
#     def countNonleaf(self,root):
#     	if(root == None or (root.l==None and root.r==None)):
#     		return 0;
#     	return 1 + self.countNonleaf(root.l) + self.countNonleaf(root.r);
#     
#==============================================================================
    def getNonLeafNodeList(self):
        self.nonLeafList = list()
        self._getNonLeafList(self.root)
        return self.nonLeafList
    
    def _getNonLeafList(self,root):
        if(root.l!=None or root.r!=None):
            self.nonLeafList.append(root)
        if(root.l!=None):
            self._getNonLeafList(root.l)
        if(root.r!=None):
            self._getNonLeafList(root.r)
        return
    
#==============================================================================
# tree = Tree()
# root = tree.addLeft(None,"wesley")
# honor = tree.addLeft(root,"honor")
# tree.addRight(root,"0")
# barclay = tree.addLeft(honor,"barclay")
# tree.addLeft(barclay,"1")
# tree.addRight(barclay,"0")
# tea = tree.addRight(honor,"tea")
# tree.addRight(tea,"1")
# tree.addLeft(tea,"0")
#  
# tree.printTree()
#==============================================================================