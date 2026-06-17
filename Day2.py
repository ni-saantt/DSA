#find largest no 
num = list(map(int,input('enter the number').split()))
laregst = nums[0]

for nu in num:
    if nu>largest:
        largest = nu
print(largest)


#print numbers using a loop 
val = list(map(int,input('enter the values').split()))
for i in range(len(val)):
    print(val[i])
#or we can do this in other way
# like 
# for num in val:
# print(num)
#What's the difference? in both so  for i in loop give output 
# 0 vale 
# 1 value 
# 2 value soo on whole for num in val: will give output 
# value 
# value 
# #value     