# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 22:43:04 2017

@author: Akshay Mehra (mehra.42@osu.edu)
"""
from collections import namedtuple
import sys
from math import log
from Data import *
from random import randint
DtNode = namedtuple("DtNode", "fVal, nPosNeg, gain, left, right")

POS_CLASS = 'e'

def Entropy(data):
    if len(data)==0:
        return 0
    positive=0
    negative=0
    for example in data:
        if example[0]==POS_CLASS:
            positive+=1
        else:
            negative+=1
    
    if positive==0 or negative==0:
        return 0.0
        
    prob_positive=float(positive)/float(len(data))
    prob_negative=float(negative)/float(len(data))
    
    H=(-1*prob_positive*log(prob_positive,2.0)) + (-1*prob_negative*log(prob_negative,2.0))
    
    return H

def InformationGain(data, f):
    #TODO: compute information gain of this dataset after splitting on feature F
    if len(data)==0:
        return 0.0
    
    data_with_f=[]
    data_without_f=[]
    for ex in data:
        if ex[f.feature]==f.value:
            data_with_f.append(ex)
        else:
            data_without_f.append(ex)
    
    prob_with_f=float(len(data_with_f))/float(len(data))
    prob_without_f=float(len(data_without_f))/float(len(data))
    H_with_f=float(Entropy(data_with_f))
    H_without_f=float(Entropy(data_without_f))
    
    Total = float(prob_with_f*H_with_f)+float(prob_without_f*H_without_f)
    IG=Entropy(data)-Total
    return IG

def Classify(tree, instance):
    if tree.left == None and tree.right == None:
        return tree.nPosNeg[0] > tree.nPosNeg[1]
    elif instance[tree.fVal.feature] == tree.fVal.value:
        return Classify(tree.left, instance)
    else:
        return Classify(tree.right, instance)

def Accuracy(tree, data):
    nCorrect = 0
    for d in data:
        if Classify(tree, d) == (d[0] == POS_CLASS):
            nCorrect += 1
    return float(nCorrect) / len(data)

def PrintTree(node, prefix=''):
    print("%s>%s\t%s\t%s" % (prefix, node.fVal, node.nPosNeg, node.gain))
    if node.left != None:
        PrintTree(node.left, prefix + '-')
    if node.right != None:
        PrintTree(node.right, prefix + '-')        
        
def ID3(data, features, MIN_GAIN=0.1):
    #TODO: implement decision tree learning       
    positive=0
    negative=0
    for example in data:
        if example[0]==POS_CLASS:
            positive+=1
        else:
            negative+=1

    if positive == len(data):
        child=DtNode(FeatureVal('Predict ','e'),(positive, negative),0.0,None,None)
        return child
    elif negative == len(data):
        child=DtNode(FeatureVal('Predict ','p'),(positive, negative),0.0,None,None)
        return child
        
    if len(features) == 0:
        if positive > negative:
            child=DtNode(FeatureVal('Predict ','e'),(positive, negative),0.0,None,None)
            return child
        else:
            child=DtNode(FeatureVal('Predict ','p'),(positive, negative),0.0,None,None)
            return child
    
    best_feature=FeatureVal(None,'0')
    max_gain=MIN_GAIN
    maxi = 0.0
    fea=sorted(features)
    for f in fea:
        feature_gain=InformationGain(data, f)
        maxi=max(maxi,feature_gain)
        if feature_gain>max_gain:
            best_feature=f 
            max_gain=feature_gain
        
    if best_feature.feature == None:
        if positive > negative:
            child=DtNode(FeatureVal('Predict ','e'),(positive, negative),maxi,None,None)
            return child
        else:
            child=DtNode(FeatureVal('Predict ','p'),(positive, negative),0.0,None,None)
            return child
    
    data_with_best_feature=[]
    data_without_best_feature=[]
    for ex in data:
        if ex[best_feature.feature]==best_feature.value:
            data_with_best_feature.append(ex)
        else:
            data_without_best_feature.append(ex)
    
    root=DtNode(best_feature,(positive,negative),max_gain,None,None)
    
    if len(data_with_best_feature)==0:        
        if positive > negative:
            child=DtNode(FeatureVal('Predict ','e'),(positive, negative),0.0,None,None)
            return child
        else:
            child=DtNode(FeatureVal('Predict ','p'),(positive, negative),0.0,None,None)
            return child
    else:
        features.discard(best_feature)        
        root=root._replace(left=ID3(data_with_best_feature, features, MIN_GAIN), right=ID3(data_without_best_feature, features, MIN_GAIN))
    return root

if __name__ == "__main__":
    train = MushroomData(sys.argv[1])
    dev = MushroomData(sys.argv[2])    
    dTree = ID3(train.data, train.features, MIN_GAIN=float(sys.argv[3]))
    PrintTree(dTree)
    print(Accuracy(dTree, dev.data))