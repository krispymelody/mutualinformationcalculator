# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:11:07 2018

@author: Pan
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 19:26:54 2018

@author: Pan
"""
'''
https://stackoverflow.com/questions/20491028/optimal-way-to-compute-pairwise-mutual-information-using-numpy?answertab=votes#tab-top
'''

import numpy as np
import pandas as pd


# read in data
df = pd.read_csv('C:/Users/Pan/Desktop/norm_sandp.csv')
data = df*100

# create stocahstic column: sandp lower than 0 is marked -1
# sandp from 0 to 1 is marked 0, sandp from 1 and up is marked 1 
def sp_tonum(row):
    if row['S&P'] < 0:
        val = -1
    elif row['S&P'] < 1:
        val = 0
    else:
        val = 1
    return val

def stock_tonum(row):
    if row['Stock'] < 0:
        val = -1
    elif row['Stock'] < 1:
        val = 0
    else:
        val = 1
    return val
data['sp'] = data.apply(sp_tonum, axis=1)
sandp = data['sp'].values
sandp = list(sandp)

data['sto'] =  data.apply(stock_tonum, axis=1)
stock = data['sto'].values
stock = list(stock)

# rename -1 to d for down, 0 to s for stay and 1 to u for up
def num_totxt(x):
    for i in range(len(x)):
        t = x[i]
        if t == -1:
            x[i] = 'd'
        if t == 0:
            x[i] = 's'
        if t == 1:
            x[i] = 'u'
            
num_totxt(sandp)
num_totxt(stock)
# print("sandp: {0}".format(sandp))
# print("stock: {0}".format(stock))


sandp = ''.join(list(sandp))
stock = ''.join(list(stock))

double = {}
for i in range(len(sandp)-1):
    t1 = sandp[i]
    t2 = stock[i]
    if t1+t2 in double: 
        double[t1 + t2] += 1
    else:
        double[t1 + t2] = 1

dcount = list(double.values())
dtotal = sum(dcount)
dprob = dcount/dtotal

def entropy(ls):
    sum = 0
    for i in ls:
        a = -i * log2(i)
        sum = sum + a
    return sum

print("markovchain: {0}".format(double))
print("Joint Entropy: {0}".format(entropy(dprob)))
# 1.2942 is the entropy of S&P, x is entropy of stock and y is mutual entropy
def mi(x,y):
    result = 1.2942 + x - y
    return result

    
    