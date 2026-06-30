# DAy5 - Simple duplicate removal script with comment hashtags.

"""
This script demonstrates a straightforward way to remove duplicates from a list while preserving order.
Hashtags (comments) are added to explain each step.
"""

# --- Section: Function ---

from decimal import HAVE_THREADS
def remove_duplicates(nums: list[int]) -> list[int]:
    """Return a list with duplicates removed while preserving order.
    Hashtags are added as comments to explain each step.
    """
    # remove duplicates from sorted array sooo
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique

# --- Section: Demo Usage ---
if __name__ == "__main__":
    # Example usage: read numbers from input and display the deduped list.
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    result = remove_duplicates(nums)
    print("Deduped list:", result)


# ---Given an array arr[] consisting of only 0's and 1's. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

left = 0 
right = len(arr)-1

while left < right :
    while left < right and arr[left]== 0:
        left += 1
    while left < right and arr[right]==1:
        right -= 1
    if left < right :
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1


# now lets come back toooo remove dublicate via 2 pointer :
#brute method was :
unique = []
for num in nums :
    if num not in unique:
        unique.append(num)
    for i in range(len(nums)):
        nums[i]=unique[i]
#2 pointer array method 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0 
        for right in range(1,len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left + 1        
          
#2 pointer linked list method
current = Head
while cureent and current.next:
             if current.value == current.next.value:
                current.next = current.next.next
             else :
                current = current.next
                