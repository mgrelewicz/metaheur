# -*- coding: utf-8 -*-
"""
Created on Sun Apr 05 15:13:37 2020
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
import random
from random import seed
from random import sample
import copy
import math
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
tabu_diff = 0
hill_diff = 0
sa_diff = 0

##### Losowanie zbioru:
print('')
print('Trwa przygotowanie danych.........')
seed(1)
sequence = [i for i in range(90)]
#print ('sequence: ', sequence)
subset = sample(sequence, 33)
#print ('subset: ', subset)
size = len(subset)

if (size%2 == 0):
    A_size = size//2
    B_size = A_size
else:
    A_size = size//2
    size += 1
    B_size = size//2
    size -= 1
#print('sizeA: ', A_size)
#print('sizeB: ', B_size)   

for i in range(0, A_size, 1):
    subset_A.append(subset[i])
for j in range(A_size, size, 1):
    subset_B.append(subset[j])
#print('subsetA: ', subset_A)   
#print('subsetB: ', subset_B)
   
sum_A = sum(subset_A)
sum_B = sum(subset_B)
#print('SumA: ', sum_A)
#print('SumB: ', sum_B)
diff = abs(sum_A - sum_B)

empty = []
initial_solution = [subset, empty]


######################### Funkcja Celu:

def objective_function(initial_solution):

    sum_A = sum(initial_solution[0])
    sum_B = sum(initial_solution[1])
    diff = abs(sum_A - sum_B)
    
    if diff == 0:
        print('bingo!')
    else:
        if sum_A > sum_B:
            #n = len(initial_solution[0])
            #i = random.randrange(0, m-1)
            sel1 = initial_solution[0].pop(0)
            #sel2 = initial_solution[1].pop(i)
            #initial_solution[0].append(sel2)
            initial_solution[1].append(sel1)
        else:
        #     m = len(initial_solution[1])
        #     #i = random.randrange(0, m-1)
        #     #sel1 = initial_solution[0].pop(i)
            sel2 = initial_solution[1].pop(0)
            initial_solution[0].append(sel2)
        #     #initial_solution[1].append(sel1)
        
        current_solution = initial_solution
        
        sum_A = sum(current_solution[0])
        sum_B = sum(current_solution[1])
        diff = abs(sum_A - sum_B)
        #print('Diff: ', diff)
    
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
    
    #print('Karmarkar-Karp return kk-diff: ', kar_diff)
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
        

    #print('Greedy_diff : ', greedy_diff)
    return greedy_diff
        

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



######################### Hill Climbing Objective Function:

def hc_objective_function(initial_solution):

    sum_A = sum(initial_solution[0])
    sum_B = sum(initial_solution[1])
    diff = abs(sum_A - sum_B)
    
    if diff == 0:
        print('bingo!')
    else:
        if sum_A > sum_B:
            n = len(initial_solution[0])
            #i = random.randrange(0, m-1)
            sel1 = initial_solution[0].pop(n-1)
            #sel2 = initial_solution[1].pop(i)
            #initial_solution[0].append(sel2)
            initial_solution[1].append(sel1)
        
        current_solution = initial_solution
        
        sum_A = sum(current_solution[0])
        sum_B = sum(current_solution[1])
        diff = abs(sum_A - sum_B)
        #print('Diff: ', diff)
    
    return diff

############################ Hill Climbing:

def hill_climbing(initial_solution):

    hc_init_sol = copy.deepcopy(initial_solution)
    current_solution = hc_init_sol
    best_minimum = hc_objective_function(current_solution)
    store_best_minimum = []
    current_minimum = hc_objective_function(current_solution)
    
    for i in range(66):       
        current_minimum = hc_objective_function(current_solution)
        if current_minimum > best_minimum:
            accept = False #odrzucamy gorsze rozwiązanie
        else:
            accept = True
        if accept==True:
            best_solution = current_solution # best solution update 
            best_minimum = hc_objective_function(best_solution)
            #if best_minimum == 0:
        else:
            break
 
        
        print('iteration: {}, best_minimum: {}'.format(i, best_minimum))
        store_best_minimum.append(best_minimum)
    
    hill_diff = min(store_best_minimum)
    print('Best diff: ', hill_diff)
    
    return hill_diff
 
    
######################### Simulated annealing Objective Function:

def sa_objective_function(initial_solution):

    sum_1 = sum(initial_solution[0])
    sum_2 = sum(initial_solution[1])
    s_diff = abs(sum_1 - sum_2)
    
    if s_diff == 0:
        print('bingo!')
    else:
        if sum_1 > sum_2:
            n = len(initial_solution[0])
            i = random.randrange(1, 3)
            sel1 = initial_solution[0].pop(n-i)
            #sel2 = initial_solution[1].pop(i)
            #initial_solution[0].append(sel2)
            initial_solution[1].append(sel1)
        else:
            m = len(initial_solution[1])
            i = random.randrange(0, 2)
            #sel1 = initial_solution[0].pop(i)
            sel2 = initial_solution[1].pop(i)
            initial_solution[0].append(sel2)
            #initial_solution[1].append(sel1)
        
        current_solution = initial_solution
        
        sum_1 = sum(current_solution[0])
        sum_2 = sum(current_solution[1])
        s_diff = abs(sum_1 - sum_2)
        #print('Diff: ', diff)
    
    return s_diff


############################ Simulated annealing:

def simulated_annealing(initial_solution):

    T_initial = 650
    T_minimum = 50
    cooling_rate = 0.97
    T_current = T_initial
    
    sa_init_sol = copy.deepcopy(initial_solution)
    current_solution = sa_init_sol
    best_cost = sa_objective_function(current_solution)
    current_cost = sa_objective_function(current_solution)
    store_best_cost = []
    
    dEn = 1
    n = 1 
    
    while T_current > T_minimum:
        for i in range(90):     # ile razy zminiejszamy temperaturę
            for j in range(1):  # dla każdego obniżenia T ile razy szukamy "sąsiada"    
                current_cost = sa_objective_function(current_solution)
                En = abs(current_cost - best_cost)

                if current_cost > best_cost:
                    En = math.exp(-En/(dEn*T_current))
                    accept = False
                else:
                    accept = True
                if accept==True:
                    best_solution = current_solution 
                    best_cost = sa_objective_function(best_solution)
                    n = n + 1       #ile zaakceptowanych
                    dEn = (dEn *(n-1) + En)/n 
                else:
                    break
                
            T_current = T_current*cooling_rate
            store_best_cost.append(best_cost)
            print('iteration: {}, best_cost: {}, T_current: {}'.format(i, best_cost, T_current))

    sa_diff = min(store_best_cost)
    print('Best diff: ', sa_diff)
    
    return sa_diff
 
    
############################ Tabu:

def tabu(subset_A, subset_B):

    sum_A = sum(subset_A)
    sum_B = sum(subset_B)
    initial_diff = abs(sum_A - sum_B)
    
    t_initial_solution = [subset_A, subset_B]
    current_solution = t_initial_solution
    candidates = []
    current_diff = initial_diff
    best_cost = 0
    store_best_cost = []
    
    # utworzenie kandydatów:
    for i in range(99):       
        if sum_A > sum_B:
            n = len(t_initial_solution[0])
            j = random.randrange(0, n-1)
            sel1 = t_initial_solution[0].pop(j)
            current_solution[1].append(sel1)
            sum_A = sum(current_solution[0])
            sum_B = sum(current_solution[1])
            current_diff = abs(sum_A - sum_B)
        else:
            m = len(t_initial_solution[1])
            k = random.randrange(0, m-1)
            sel2 = t_initial_solution[1].pop(k)
            current_solution[0].append(sel2)
            sum_A = sum(current_solution[0])
            sum_B = sum(current_solution[1])
            current_diff = abs(sum_A - sum_B)
        
        if current_diff < initial_diff:
            candidates.append([current_solution[0], current_solution[0]]) 
            best_cost = current_diff
            store_best_cost.append(best_cost)
        print('iteration: {}, best_cost: {}'.format(i, best_cost))

    # wyodrębnienie najlepszego kandydata
    lc = len(store_best_cost)      
    for i in range(lc-1):             
        if store_best_cost[i] == 0:
            print('bingo!')
        else:
            best_cost_so_far = min(store_best_cost)
            store_best_cost.append(best_cost_so_far)
    
    tabu_diff = min(store_best_cost)
    print('Best diff: ', tabu_diff)
    
    return tabu_diff    

############################ Funkcja oceny:

def main():
    
    #print(subset)
    seq2 = [i for i in range(10000)]
    sub_ext1 = sample(seq2, 55)
    sub_ext2 = sample(seq2, 155)
    sub_ext3 = sample(seq2, 255)
    sub_ext4 = sample(seq2, 355)
    sub_ext5 = sample(seq2, 455)
#    sub_ext6 = sample(seq2, 555)
#    sub_ext7 = sample(seq2, 655)
#    sub_ext8 = sample(seq2, 755)
#    sub_ext9 = sample(seq2, 855)
#    sub_ext10 = sample(seq2, 955)
#    sub_ext11 = sample(seq2, 1055)
#    sub_ext12 = sample(seq2, 1155)
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
    #sub_list = [sub_ext1, sub_ext2, sub_ext3, sub_ext4, sub_ext5, sub_ext6, sub_ext7, sub_ext8, sub_ext9, sub_ext10, sub_ext11, sub_ext12]
    ## krótki test:
    #sub_list = [sub_ext1, sub_ext2, sub_ext3, sub_ext4, sub_ext5]
    ## tylko 2 przebiegi:
    #sub_list = [sub_ext1, sub_ext2]
    ## tylko 1 przebieg:
    sub_list = [sub_ext1]
    
    bf_time_sum = 0
    bf_time_avg = 0
    g_time_sum = 0
    g_time_avg = 0
    kk_time_sum = 0
    kk_time_avg = 0
    tabu_time_sum = 0
    tabu_time_avg = 0
    hill_time_sum = 0
    hill_time_avg = 0
    sa_time_sum = 0
    sa_time_avg = 0
    avg_min = 0
    avg_all = []
    g_reply = []
    bf_reply = []
    kk_reply = []
    tabu_reply = []
    hill_reply = []
    sa_reply = []


    print("")
    print(">>> start kalkulacji <<<")
    print("")
    
    subset1 = subset
    for sub_ext in sub_list:
        start1 = time.time()
        greedy_diff = greedy(subset1)
        g_reply.append(greedy_diff)
        end1 = time.time()
        g_time=((end1 - start1))  #/10?
        #print ("Greedy: Czas %f s" % (g_time))
        subset1.extend(sub_ext)
        #g_time=((end1 - start1)/10)
        g_time_sum += g_time
    g_time_avg = g_time_sum/len(sub_list)
    avg_all.append(round(g_time_avg, 5))
    # print('Greedy czas sredni: ', g_time_avg)
    # print('')
    
## ! bf wiesza się przy większych danych
    subset2 = subset
    for sub_ext in sub_list:
        start2 = time.time()
        brute(subset2)
        bf_reply.append(str(brute(subset2)))
        end2 = time.time()
        bf_time=((end2 - start2)/10)
        ##print(subset2, brute_check)
        #print ("BruteForce: Czas %f s" % (bf_time))
        subset2.extend(sub_ext)
        bf_time_sum += bf_time
    bf_time_avg = bf_time_sum/len(sub_list)
    avg_all.append(round(bf_time_avg, 5))
    # print('BruteForce czas sredni: ', bf_time_avg)
    # print('')
    
    subset3 = subset
    for sub_ext in sub_list:
        start3 = time.time()
        kar_diff = karp(subset3)
        kk_reply.append(kar_diff)
        end3 = time.time()
        kk_time=((end3 - start3))
        #print ("KK: Czas %f s" % (kk_time))
        subset3.extend(sub_ext)
        kk_time_sum += kk_time
    kk_time_avg = kk_time_sum/len(sub_list)
    avg_all.append(round(kk_time_avg, 5))
    # print('Karmarkar czas sredni: ', kk_time_avg)        
    # print('')
    
    subset5a = subset_A
    subset5b = subset_B
    print('Tabu:')
    for sub_ext in sub_list:
        start5 = time.time()
        tabu_diff = tabu(subset5a, subset5b)
        tabu_reply.append(tabu_diff)
        end5 = time.time()
        tabu_time=((end5 - start5))
        #print ("Tabu search: Czas %f s" % (tabu_time))
        # subset5a.extend(sub_ext)
        # subset5b.extend(sub_ext)
        tabu_time_sum += tabu_time
    tabu_time_avg = tabu_time_sum/len(sub_list)
    avg_all.append(round(tabu_time_avg, 5))
    print('Tabu Search czas sredni: ', tabu_time_avg)      
    print('')
    
    subset6 = initial_solution
    print('Hill Climbing:')
    for sub_ext in sub_list:
        start6 = time.time()
        hill_diff = hill_climbing(subset6)
        hill_reply.append(hill_diff)
        end6 = time.time()
        hill_time=((end6 - start6))
        #print ("Hill Climbing: Czas %f s" % (hill_time))
        #subset6.extend(sub_ext)
        hill_time_sum += hill_time
    hill_time_avg = hill_time_sum/len(sub_list)
    avg_all.append(round(hill_time_avg, 5))
    print('Hill Climbing czas sredni: ', hill_time_avg)        
    print('')
    
    subset7 = initial_solution
    print('Simulated Annealing:')
    for sub_ext in sub_list:
        start7 = time.time()
        sa_diff = simulated_annealing(subset7)
        sa_reply.append(sa_diff)
        end7 = time.time()
        sa_time=((end7 - start7))
        #print ("SA: Czas %f s" % (sa_time))
        #subset7.extend(sub_ext)
        sa_time_sum += sa_time
    sa_time_avg = sa_time_sum/len(sub_list)
    avg_all.append(round(sa_time_avg, 5))
    print('Simulated Annealing czas sredni: ', sa_time_avg)        
    print('')
    
    print(">>> koniec kalkulacji <<<")
    print('')


### odpowiedzi algorytmów:
    print('')    
    print('Odpowiedzi algorytmów:')
    print('')

    print("Karmarkar-Karp: ", kk_reply)
    if kar_diff == 0:
        print("KK: Da się podzielić na dwa podzbiory o rownej sumie") 
    if kar_diff != 0: 
        print("KK: Nie da się podzielić na dwa podzbiory o rownej sumie") 
    print('')
    print("Greedy: ", g_reply)
    if greedy_diff == 0:
        print("Greedy: Da się podzielić na dwa podzbiory o rownej sumie")
    if greedy_diff != 0:
        print("Greedy: Nie da się podzielić na dwa podzbiory o rownej sumie")
    print('')
    print("BruteForce: ", bf_reply)
    brute_reply = str(brute(subset))
    if brute_reply == True:
        print("BF: Da się podzielić na dwa podzbiory o rownej sumie")
    if brute_reply == False:
        print("BF: Nie da się podzielić na dwa podzbiory o rownej sumie")
    print('')
    print("Tabu Search: ", tabu_reply)
    if tabu_diff == 0:
        print("Tabu Search: Da się podzielić na dwa podzbiory o rownej sumie") 
    if tabu_diff != 0: 
        print("Tabu Search: Nie da się podzielić na dwa podzbiory o rownej sumie")    
    print('')
    print("Hill Climbing: ", hill_reply)
    if hill_diff == 0:
        print("Hill Climbing: Da się podzielić na dwa podzbiory o rownej sumie") 
    if hill_diff != 0: 
        print("Hill Climbing: Nie da się podzielić na dwa podzbiory o rownej sumie")
    print('')
    print("Simulated Annealing: ", sa_reply)
    if sa_diff == 0:
        print("SA: Da się podzielić na dwa podzbiory o rownej sumie") 
    if sa_diff != 0: 
        print("SA: Nie da się podzielić na dwa podzbiory o rownej sumie")

        
### finalna ocena:
    print('')
    print('Średnie czasy (greedy, brute, kk, tabu, hill, sa): ', avg_all)
    print('')    
    
    avg_min = min(avg_all)    
    
    if (kk_time_avg == avg_min):
        print('Najszybszym algorytmem jest: Karmarkar-Karp')
    if (bf_time_avg == avg_min):
        print('Najszybszym algorytmem jest: Brute Force')
    if (g_time_avg == avg_min):
        print('Najszybszym algorytmem jest: Greedy')
    if (tabu_time_avg == avg_min):
        print('Najszybszym algorytmem jest: Tabu Search')
    if (hill_time_avg == avg_min):
        print('Najszybszym algorytmem jest: Hill Climbing')
    if (sa_time_avg == avg_min):
        print('Najszybszym algorytmem jest: Simulated Annealing')
    
        
main()
    
###############################################################################
