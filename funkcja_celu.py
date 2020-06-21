# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:13:37 2020

@author: Marcin
"""
#


#### Funkcja celu: chcemy uzyskać różnicę (diff) żeby móc ją minimalizować
    
def target(subset):
    
    size = len(subset)
    print('size: ', size)
    
    if (size%2 == 0):
        A_size = size//2
        B_size = size//2
    else:
        A_size = size//2
        size += 1
        B_size = size//2
        size -= 1
    print('sizeA: ', A_size)
    print('sizeB: ', B_size)   
    
    for i in range(0, A_size, 1):
        subset_A.append(subset[i])
    for j in range(A_size, size, 1):
        subset_B.append(subset[j])
    print('subsetA: ', subset_A[:5])   
    print('subsetB: ', subset_B[:5])   
    
    sum_A = sum(subset_A)
    sum_B = sum(subset_B)
    print('SumA: ', sum_A)
    print('SumB: ', sum_B)
    
    if (sum_A >= sum_B):
        diff = (sum_A - sum_B)
    else:
        diff = (sum_B - sum_A)
    
    print('Diff: ', diff)
    if diff == 0:
        print('bingo!')
    else:
        print('Potrzebna optymalizacja!')
    
    #return Output()
    return diff

