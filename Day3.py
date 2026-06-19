# 2 num sum problem 

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} #createss a empty directory 
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen :
                return [seen[diff], i ]    #returning the index of that no and the cureent index no 
            seen[nums[i]]=i    #or else save that diff iwith in dex in seen