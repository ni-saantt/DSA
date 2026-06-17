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


#Take n numbers as input and print only the even numbers from the list
# and now to count no of even nos in this 
n = int(input('enter the no of elements'))
ff = list(map(int,input('enter the values').split()))[:n]
count = 0
for va in ff:
    if va % 2 == 0 :
        print(va)
        count +=1
print(count)

# another method for this is 
 n = int(input('enter the no of elements'))
 ff = []
 for i in range(n):
    num = int(input('enter the num'))
    ff.append(num)
 for va in ff:
    if va % 2 == 0 :
        print(va)
   
