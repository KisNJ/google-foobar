nums=[1,2,3,4,5]
nums2=tuple(n for n in nums if n%2==0)
nums[0]=7

print(nums2)
print("s" in "string")


gen=(n*n for n in nums)
gen2=(n*n for n in nums)
for g in gen:
    print (g)


for g in gen2:
    print (g)



matrix =[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(zip(*matrix))
first=[1,2,3]
second=['a','b','c']
print(list(zip(first,second)))

nested=[[1,2,3]]
print(tuple(n for n in list(*nested)))