# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:13:37 2020

@author: Marcin
"""
#
## Partition problem is to determine whether a given set can be partitioned
## into two subsets such that the sum of elements in both subsets is same. 
#
###############################################################################
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
import copy
#import math
import time

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
sequence = [i for i in range(90)]
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


######################### Algorytm Karmarkar-Karp:

def karp(subset):
    
    ksubset = copy.deepcopy(subset)
    
    while True:
        max1 = max(ksubset)
        index1 = ksubset.index(max1)
        ksubset[index1] = 0
        max2 = max(ksubset)
        if max2 == 0:
            break
        index2 = ksubset.index(max2)
        ksubset[index1] = abs(max1 - max2)
        ksubset[index2] = 0
        kar_diff = ksubset[index1]
    
    print('Karmarkar-Karp return kk-diff: ', kar_diff)
    return kar_diff


######################### Algorytm zachłanny:

def greedy(subset):
    
    subset_A = []
    subset_B = []
    sum_A = 0
    sum_B = 0
#    print('Greedy przed:')
#    print('subset A: ', subset_A)
#    print('subset B: ', subset_B)
#    print('Sum subset_A : ', sum(subset_A))
#    print('Sum subset_B : ', sum(subset_B))
    for n in sorted(subset, reverse=True):
        if sum_A < sum_B:
           subset_A.append(n)
           sum_A = sum(subset_A)
           sum_B = sum(subset_B)
        else:
           subset_B.append(n)
           sum_A = sum(subset_A)
           sum_B = sum(subset_B)

#    print('Greedy po:')
#    print('subset A: ', subset_A)
#    print('subset B: ', subset_B)
#    print('Sum subset_A : ', sum(subset_A))
#    print('Sum subset_B : ', sum(subset_B))
    
    if sum_A == sum_B:
        greedy_diff = 0
    else:
        if (sum_A >= sum_B):
            greedy_diff = (sum_A - sum_B)
        else:
            greedy_diff = (sum_B - sum_A)
        

    print('Greedy_diff : ', greedy_diff)
    return (greedy_diff)   
        

########################### rekursywny Brute-Force :
#
### ! Złożonosc tego algorytmu to exponential O(2^n) !
##
def brute(subset):
    
    sum_subset = sum(subset)
    #t = Output()
    
    if sum_subset % 2 != 0:
        return False
        
    return brute_recursive(subset, sum_subset / 2, 0)

def brute_recursive(subset, sum, currentIndex):
  
    if sum == 0:
        return True
    
    n = len(subset)
    if n == 0 or currentIndex >= n:
        #print('false')
        return False

# wywołanie rekurencyjne po wybraniu numeru na bieżącym indeksie
# jeśli liczba na indeksie przekracza sumę, pomijamy
    if subset[currentIndex] <= sum:
        if(brute_recursive(subset, sum - subset[currentIndex], currentIndex + 1)):
            return True
        
# wywołanie rekurencyjne po wykluczeniu numeru na bieżącym indeksie
    return brute_recursive(subset, sum, currentIndex + 1)



############################### Dynamic Programming :

def dynPro(subset, size): 
    
    s_sum = 0
    i, j = 0, 0
       
    for i in range(size): 
        s_sum += subset[i] 
      
    if s_sum % 2 != 0: 
        return False 
      
    part = [[ True for i in range(size + 1)]  
                   for j in range(s_sum // 2 + 1)] 
      
    # inicjuje górny wiersz 
    for i in range(0, size + 1): 
        part[0][i] = True
          
    # inicjalizuje skrajną lewą kolumnę,  
    # oprócz part[0][0], jako 0 
    for i in range(1, s_sum // 2 + 1): 
        part[i][0] = False
      
    # wypełnia tablicę od dołu do góry  
    for i in range(1, s_sum // 2 + 1): 
          
        for j in range(1, size + 1): 
            part[i][j] = part[i][j - 1] 
              
            if i >= subset[j - 1]: 
                part[i][j] = (part[i][j] or 
                              part[i - subset[j - 1]][j - 1]) 
          
    return part[s_sum // 2][size] 
      


############################ Funkcja oceny:


def main():
    
    target(subset)
    #print(subset)
    seq2 = [i for i in range(10000)]
    sub_ext1 = sample(seq2, 55)
    sub_ext2 = sample(seq2, 155)
    sub_ext3 = sample(seq2, 255)
    sub_ext4 = sample(seq2, 355)
    sub_ext5 = sample(seq2, 455)
    sub_ext6 = sample(seq2, 555)
    sub_ext7 = sample(seq2, 655)
    sub_ext8 = sample(seq2, 755)
    sub_ext9 = sample(seq2, 855)
    sub_ext10 = sample(seq2, 955)
    sub_ext11 = sample(seq2, 1055)
    sub_ext12 = sample(seq2, 1155)
#    sub_ext13 = sample(seq2, 1255)
#    sub_ext14 = sample(seq2, 1355)
#    sub_ext15 = sample(seq2, 1455)
#    sub_ext16 = sample(seq2, 1555)
#    sub_ext17 = sample(seq2, 1655)
#    sub_ext18 = sample(seq2, 1755)
#    sub_ext19 = sample(seq2, 1855)
#    sub_ext20 = sample(seq2, 1955)
#    sub_ext21 = sample(seq2, 2055)
#    sub_ext22 = sample(seq2, 2155)
#    sub_ext23 = sample(seq2, 2255)
#    sub_ext24 = sample(seq2, 2355)
#    sub_ext25 = sample(seq2, 2555)
    
    ## wszystkie próbki:
    #sub_list = [sub_ext1, sub_ext2, sub_ext3, sub_ext4, sub_ext5, sub_ext6, sub_ext7, sub_ext8, sub_ext9, sub_ext10, sub_ext11, sub_ext12, sub_ext13, sub_ext14, sub_ext15, sub_ext16, sub_ext17, sub_ext18, sub_ext19, sub_ext20, sub_ext21, sub_ext22, sub_ext23, sub_ext24, sub_ext25]
    ## połowa:
    sub_list = [sub_ext1, sub_ext2, sub_ext3, sub_ext4, sub_ext5, sub_ext6, sub_ext7, sub_ext8, sub_ext9, sub_ext10, sub_ext11, sub_ext12]
    ## krótki test:
    #sub_list = [sub_ext1, sub_ext2, sub_ext3, sub_ext4, sub_ext5]
    ## tylko 2 przebiegi:
    #sub_list = [sub_ext1, sub_ext2]
    
    bf_time_sum = 0
    bf_time_avg = 0
    g_time_sum = 0
    g_time_avg = 0
    kk_time_sum = 0
    kk_time_avg = 0
    dp_time_sum = 0
    dp_time_avg = 0
    avg_max = 0
    avg_all = []
    g_reply =[]
    dp_reply =[]
    kk_reply =[]
#    bf_reply =[]

    print("")
    print(">>> start kalkulacji <<<")
    print("")
    

    subset1 = subset
    for sub_ext in sub_list:
        start1 = time.time()
        greedy(subset1)
        g_reply.append(greedy_diff)
        end1 = time.time()
        g_time=((end1 - start1))  #/10?
        print ("Greedy: Czas %f s" % (g_time))
        subset1.extend(sub_ext)
        #g_time=((end1 - start1)/10)
        g_time_sum += g_time
    print("")
    g_time_avg = g_time_sum/len(sub_list)
    avg_all.append(g_time_avg)
    print('Greedy czas sredni: ', g_time_avg)
    print('')
    
## ! bf wiesza się przy większych    
#    subset2 = subset
#    for sub_ext in sub_list:
#        start2 = time.time()
#        brute(subset2)
##        bf_reply.append(str(brute(subset2)))
#        end2 = time.time()
#        bf_time=((end2 - start2)/10)
#        ##print(subset2, brute_check)
#        print ("BruteForce: Czas %f s" % (bf_time))
#        subset2.extend(sub_ext)
#        bf_time_sum += bf_time
#    print("")
#    bf_time_avg = bf_time_sum/len(sub_list)
#    avg_all.append(bf_time_avg)
#    print('Brute czas sredni: ', bf_time_avg)
#    print('')


    subset3 = subset
    for sub_ext in sub_list:
        start3 = time.time()
        karp(subset3)
        kk_reply.append(kar_diff)
        end3 = time.time()
        kk_time=((end3 - start3))
        print ("KK: Czas %f s" % (kk_time))
        subset3.extend(sub_ext)
        kk_time_sum += kk_time
        print("")
    kk_time_avg = kk_time_sum/len(sub_list)
    avg_all.append(kk_time_avg)
    print('Karmarkar czas sredni: ', kk_time_avg)        
    print('')
    
    
    subset4 = subset
    for sub_ext in sub_list:
        start4 = time.time()
        dynPro(subset4, size)
        dp_reply.append(str(dynPro(subset4, size)))
        end4 = time.time()
        dp_time=((end4 - start4))
        print ("DP: Czas %f s" % (dp_time))
        subset4.extend(sub_ext)
        dp_time_sum += dp_time
        #print("")
    dp_time_avg = dp_time_sum/len(sub_list)
    avg_all.append(dp_time_avg)
    print('Dynamic Programming czas sredni: ', dp_time_avg)        
    print('')
    
    print(">>> koniec kalkulacji <<<")
    print('')


### odpowiedzi algorytmów:
    print('')    
    print('Odpowiedzi algorytmów:')
    print('')

    if dynPro(subset, size) == True: 
        print("DP: Da się podzielić na dwa podzbiory o rownej sumie") 
    if dynPro(subset, size) == False:  
        print("DP: Nie da się podzielić na dwa podzbiory o rownej sumie") 


    if kar_diff == 0:
        print("KK: Da się podzielić na dwa podzbiory o rownej sumie") 
    if kar_diff != 0: 
        print("KK: Nie da się podzielić na dwa podzbiory o rownej sumie") 


    if greedy_diff == 0:
        print("Greedy: Da się podzielić na dwa podzbiory o rownej sumie")
    if greedy_diff != 0:
        print("Greedy: Nie da się podzielić na dwa podzbiory o rownej sumie")


    brute_reply = str(brute(subset))
    if brute_reply == True:
        print("BF: Da się podzielić na dwa podzbiory o rownej sumie")
    if brute_reply == False:
        print("BF: Nie da się podzielić na dwa podzbiory o rownej sumie")


        
### finalna ocena:
    print('')
    print('Avg all: ', avg_all)
    print('')    
    
    avg_max = max(avg_all)    
    
    if (dp_time_avg == avg_max):
        print('Najszybszym algorytmem jest: Dynamic Programming')
    if (kk_time_avg == avg_max):
        print('Najszybszym algorytmem jest: Karmarkar-Karp')
    if (bf_time_avg == avg_max):
        print('Najszybszym algorytmem jest: Brute Force')
    if (g_time_avg == avg_max):
        print('Najszybszym algorytmem jest: Greedy')
    
### Teoretyczne porównanie do poprawnego rozwiązania - jesli bysmy je mieli:   
    print('') 
#    print('Sprawdzenie trafnosci: ')
#    print('')
#    print("Rozwiązanie: ", solution)
#    print('') 
    print("Greedy: ", g_reply)
    print('') 
    print("Dynamic Programming: ", dp_reply)
    print('') 
    print("Karmarkar-Karp: ", kk_reply)
#    print("BruteForce: ", bf_reply)
#    print('') 
    
        
        
main()
    
###############################################################################