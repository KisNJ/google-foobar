
import numpy as np
import math
from decimal import Decimal
from fractions import Fraction

def solution(m):
    returned=sort_by_absorbing(m)
    return np.array(returned)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
#print gcd(12,5)
def sort_by_absorbing(m):
    absorbing_matrix,non_absorbing_matix,removed_from_non_matrix=only_absorbing_matrix(m)
    chanches=create_matrix_with_chances(non_absorbing_matix,removed_from_non_matrix)
    substracted_inversed_matrix=matrix_substraction_inverse(chanches)
    temp_non_absorbing=[]
    for n in non_absorbing_matix:
        temp_non_absorbing.append(*list(n.values()))

    temp_of_chances=create_chanche(removed_from_non_matrix, non_absorbing_matix)
    temp_non_absorbing=[]
    for n in temp_of_chances:
        temp_non_absorbing.append(*list(n.values()))

    list_of_nums=np.matmul(np.matrix(substracted_inversed_matrix),np.matrix(temp_non_absorbing))

    half_of_list=list_of_nums[0]
    temp_half_list=half_of_list.tolist()
    temp_a=[]
    for num in temp_half_list:
        for num2 in num:
            temp_a.append(Fraction(num2).limit_denominator())


    denominators=[]

    for num in temp_a:
        if "/" in str(num):
            denominators.append(str(num).split("/")[1])

    lcm = 1
    for i in denominators:
        lcm = lcm*int(i)//gcd(lcm, int(i))
    for index,num in enumerate(*temp_half_list):
        use_this_num=Fraction(num).limit_denominator()
        if "/" in str(use_this_num):
            numerator=int(str(use_this_num).split("/")[0])
            denom=int(str(use_this_num).split("/")[1])
            if denom!=lcm:
                rate=Fraction(lcm,denom)
                numerator=numerator*rate
            temp_half_list[0][index]=Fraction(numerator,denom)
        else:
            temp_half_list[0][index]=Fraction(use_this_num,lcm)


    return_this_list=[]

    for num in temp_half_list[0]:
        if "/" in str(num):
            return_this_list.append(int(str(num).split("/")[0]))
        else:
            return_this_list.append(int(str(num)[0]))
    return_this_list.append(lcm)
    return return_this_list

def create_chanche(m1,m2):
    denoms=[]
    for index,dictionary in enumerate(m2):
        for key in list(dictionary.keys()):
            sum_=sum(dictionary[key])+sum(*list(m1[index].values()))
            denoms.append(sum_)
    for index,dictionary in enumerate(m2):
        for key in list(dictionary.keys()):
            div_by_this=denoms[index]
            dictionary[key]=[n/div_by_this for n in dictionary[key]]
    return m2

def create_matrix_with_chances(m1,m2):
    sums_for_ids=[]
    denoms=[]
    for index,dictionary in enumerate(m2):      
        for index2,key in enumerate(dictionary):
            sums_for_ids.append({key:[]})
            denoms.append({key:0})
    
    for index,dictionary in enumerate(m2):      
        for index2,key in enumerate(dictionary):
            for index3,arr in enumerate(dictionary[key]):
                for index4,dictionary2 in enumerate(sums_for_ids):
                    for index5,key2 in enumerate(dictionary2):
                        if key2==index3:
                            sums_for_ids[index4][key2].append(dictionary[key][index3])
    for index,dictionary in enumerate(m1):
        for index2,key in enumerate(dictionary):
            denoms[index][key]+=sum(dictionary[key])
    
    for index,dictionary in enumerate(m2):
        for index2,key in enumerate(dictionary):
            denoms[index][key]+=sum(dictionary[key])


    chanches=[]
    for index_of_dic,dic in enumerate(sums_for_ids):
        temp=[]
        for index,value in enumerate(list(dic.items())[0][1]):
            temp.append(value/list(denoms[index].values())[0])
        chanches.append({list(dic.keys())[0]:temp})
    return chanches


def only_absorbing_matrix(m):
    absorbing_indexes=[]
    absorbing_matrix=[]
    non_absorbing_matix=[]
    removed_from_non_matrix=[]
    for val,row in enumerate(m):
        if(row[val]==sum(row)):
            absorbing_indexes.append(val)
            absorbing_matrix.append((val,row))
        else:
            non_absorbing_matix.append((val,row))
    
    #------------
    for row_index,row in enumerate(absorbing_matrix):
        
        for index,num in enumerate(row[1]):
             if index not in absorbing_indexes:
                
                absorbing_matrix[row_index][1][index]="del me"
        
    new_row=[]
    for row_index,row in enumerate(absorbing_matrix):
        new_row=[]
        for col_index,column in enumerate(absorbing_matrix[row_index][1]):
            if(column!="del me"):
                new_row.append(column)
        absorbing_matrix[row_index]={row[0]:new_row}

    #---------------------
    for row_index,row in enumerate(non_absorbing_matix): 
        temp=[]  
        for index,num in enumerate(row[1]):
             if index not in absorbing_indexes:
                temp.append( non_absorbing_matix[row_index][1][index])
                non_absorbing_matix[row_index][1][index]="del me"
        removed_from_non_matrix.append({row[0]:temp})
    
    new_row=[]
    for row_index,row in enumerate(non_absorbing_matix):
        new_row=[]
        for col_index,column in enumerate(non_absorbing_matix[row_index][1]):
            if(column!="del me"):
                new_row.append(column)
        non_absorbing_matix[row_index]={row[0]:new_row}

    return (absorbing_matrix,non_absorbing_matix,removed_from_non_matrix)

def matrix_substraction_inverse(chanches):
    length=len(chanches)
    identity_arr=[]
    index=0
    while index<length:
        temp=[]
        for i in range(length):
            if i==index:
                temp.append(1)
            else:
                temp.append(0)
        identity_arr.append(temp)
        index+=1
    chanches_list=[]
    
    for n in chanches:
        chanches_list.append(*list(n.values()))
    chanches_list=np.transpose(chanches_list)
    
    matrix_chanches=np.matrix(chanches_list)
    matrix_identiy=np.matrix(identity_arr)
    sub=np.subtract(matrix_identiy,matrix_chanches)

    return np.linalg.inv(sub)


print(solution([
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,8,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,6,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]))