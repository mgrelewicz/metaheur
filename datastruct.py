# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:13:37 2020

@author: Marcin
"""
#

#### Input:
## Zbiór liczb, np:  {3, 1, 1, 2, 2, 1}
#### Output:
## 1) Różnica: Im mniejsza tym lepiej działa algorytm. Jesli wynosi O, zbiór da 
#  się podzielić na 2 równe częsci
## 2) Dwa podzbiory (po podziale)
#

#import random
from random import seed
from random import sample


#################### Struktury danych:

subset = []
subset_A = []
subset_B = []

sum_A = 0
sum_B = 0

sum_subset = 0

greedy_diff = 0
kar_diff = 0
brute_diff = 0
brute_check = 0


##### Losowanie zbioru:
print('')
print('Trwa przygotowanie danych.........')
seed(1)
sequence = [i for i in range(100)]
#print ('sequence: ', sequence)
subset = sample(sequence, 20)
#print ('subset: ', subset)
size = len(subset)

#class Output: 
#    def __init__(self): 
#        self.subset_A = []
#        self.subset_B = []
#        self.subset = []
#        self.diff = 0   


