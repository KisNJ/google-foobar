import random
matrix=[]

terminal=random.randint(1, 9)
# print(terminal)
# n=random.randint(1,201)
# print(n)
# print(n%2==0)
for u in range (10):
    temp=[]
    if u == terminal:
        for zero in range(10):
            temp.append(0)
    elif random.randint(1,201)%2==0:
        for zero in range(10):
            temp.append(0)
    else:
        for num in range(10):
            if num==u:
                temp.append(0)
            else:
                if random.randint(1, 201)%2==0:
                    temp.append(0)
                else:
                    temp.append(random.randint(1, 999))
    matrix.append(temp)
print(matrix)