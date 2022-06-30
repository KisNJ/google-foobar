import numpy as np

def calculate_r(m):
    active=[]
    terminal=[]
    actice_indexes=[]
    terminal_indexes=[]
   
    for index,row in enumerate(m):
        if sum(row)>0:
            active.append(row)
            actice_indexes.append(index)
        else:
            terminal.append(row)
            terminal_indexes.append(index)

    for n,row in enumerate(active):
        sum_of_this_row=sum(row)
        for n2,num in enumerate(row):
            active[n][n2]=num/float(sum_of_this_row)
    R=[]
    Q=[]
    for index,row in enumerate(active):
        tempQ=[]
        tempR=[]
        for real_index,num in enumerate(row):
            if real_index in actice_indexes:
                tempQ.append(num)
            else:
                tempR.append(num)
        R.append(tempR)
        Q.append(tempQ)
    ret_this=[]
    if 0 in terminal_indexes:
        for index,number in enumerate(terminal_indexes):
            if index==0:
                ret_this.append(1)
            else:
                ret_this.append(0)
        ret_this.append(1)
        return (ret_this,"short end")
    return (R,Q)
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def float_to_ratio(number):

    accuracy=len(str(number))-2
    if accuracy >8:
        accuracy=8
    whole_part=int(str(number)[0])
    number=float(number)
    number=number-whole_part
    number=round(number,accuracy)
    numerator=0
    denominator=1
    while round(numerator/float(denominator),accuracy)!=number and denominator<20000:
        if round(numerator/float(denominator),accuracy)>number:
            denominator+=1
            numerator
        elif numerator+1<=denominator:
            numerator+=1
        else:
            numerator=1
            denominator+=1
    numerator+=whole_part*denominator
    return (numerator,denominator)
def detect_states(matrix):
    active, terminal = [], []
    for rowN, row in enumerate(matrix):
        (active if sum(row) else terminal).append(rowN)
    
    return(active,terminal)
def simplest_form(B):
    B = B.round().astype(int).A1                   # np.matrix --> np.array
    gcd = np.gcd.reduce(B)
    B = np.append(B, B.sum())                      # append the common denom
    return (B / gcd).astype(int)
def solution(m):
    active, terminal = detect_states(m)
    m_use= np.matrix(m, dtype=float)[active, :]
    comm_denom = np.prod(m_use.sum(1))

    R_T,Q_T=calculate_r(m)

    if Q_T=="short end":
        ret=calculate_r(m)[0]
        return ret
    R=np.matrix(R_T)
    Q=np.matrix(Q_T)
    length=len(Q)
    I=np.identity(length)
    # print((((I-Q)**-1)*R).round())
    li=(((I-Q)**-1)*R)[0].tolist()
    # print((((I-Q)**-1)*R)[0])
    denominators=[]
    numerators=[]
    N = (I - Q) ** (-1)
    B = N[0] * R * comm_denom / np.linalg.det(N)
    # print(B)
    # for l in li[0]:
        
    #     num=float_to_ratio(l)
    #     if num[1]==20000:
    #         numerators.append(1)
    #         denominators.append(1)
    #     else:
    #         numerators.append(num[0])
    #         denominators.append(num[1])

    # lcm=np.lcm.reduce(denominators)
    
    # for index,num in enumerate(numerators):
    #     if denominators[index]!=lcm:
    #         numerators[index]*=lcm/float(denominators[index])      
    # for index,num in enumerate(numerators):
    #     numerators[index]=int(num)
    # numerators.append(lcm)
    #print(simplest_form(B))
    return simplest_form(B)


print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))

