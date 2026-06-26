# 2 sum problems - if we need to find index not numbers and array is not sorted we will use basic mwthod of hash map 
# if array iss sorted , or numbers are asked we will use 2 pointer 

#so lets first solve by 2 pointer  when we need numbers or array is already sorted
nums.sort() #only do when we need numbers not the index
left,right = 0, len(nums)-1 

while left < right :
    total = nums[left] + nums[right]
    if  total < target:
        left += 1
    elif total > target:
        right -=1
    else :
        return[nums[left],nums[right]]       

#another method if it was not sorted and we wanted index were hashmap
#store = {}
#for i in range(len(nums)):
#    req = target - nums[i]
#    if req in store:
#        return[store[req],i]
#    else :
#        store[nums[i]] = i
