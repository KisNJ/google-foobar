def solution(x, y):
    first_in_col=0
    for first in range(1,x+1):
        first_in_col+=first
    col=[first_in_col,first_in_col+x]
    index=1
    for first_r in range(1,y):
        col.append(col[index]+x+first_r)
        index+=1
    print(col)
    return str(col[y-1])
    # while len(rows)<x+y-1:
    #     print(rows)
    #     if len(rows)<how_many_to_add:
    #         rows.append([])
    #     if not len(rows[how_many_to_add-1])>y:
    #         rows[how_many_to_add-1].append(which_num_to_add)
    #     which_num_to_add+=1
    #     if(how_many_to_add+1>max_add):
    #         how_many_to_add=1
    #         max_add+=1
    #     else:
    #         how_many_to_add+=1
    # return str(rows[x-1][y-1])


print(solution(5,10))