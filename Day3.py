# 2 num sum problem 

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} #createss a empty directory 
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen :
                return [seen[diff], i ]    #returning the index of that no and the cureent index no 
            seen[nums[i]]=i    #or else save that diff iwith in dex in seen


#3 sum problem 
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:   #skip dublicate 
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right :
                total = nums[i] + nums[left] + nums[right]
                if total < 0 :
                    left += 1
                elif total > 0 :
                    right -= 1
                else :
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right  and nums[right] == nums[right + 1]:
                        right -= 1
        return result

# pehle sort , then ek list banaya for entering ressultss, then ek main loop i to len(nums)
# now to avoid dublication  we use if i>0 and nums[i] == nums[i-1]: continue
# fir left asssign kara and then right 
# fie jab tak left aur right meet nahi kar jata 
# total nikalo 
# and total agar - ve hai to left se ek badhao aur gar + ve hai to right ide se ek decresse  
# #and == 0 then store that in the list ressult created and usske aage  badhte jao dublication avoid karne ke sath sath                


# 3 sum closest 
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    left += 1

                elif total > target:
                    right -= 1

                else:
                    return total

        return closest