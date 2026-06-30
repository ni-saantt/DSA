# Day3 - Array utilities for sum problems.

"""
Provides solutions for:
- Two Sum
- Three Sum
- Three Sum Closest
"""

class ArrayUtilities:
    """Utility class containing static methods for array-based problems."""

    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        """Return indices of the two numbers that add up to target."""
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        raise ValueError("No two sum solution found")

    @staticmethod
    def three_sum(nums: list[int]) -> list[list[int]]:
        """Return all unique triplets that sum to zero."""
        nums.sort()
        result: list[list[int]] = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result

    @staticmethod
    def three_sum_closest(nums: list[int], target: int) -> int:
        """Return the sum of three integers closest to the target."""
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
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

if __name__ == "__main__":
    # Simple demo usage (can be removed in production).
    print("Two Sum demo:", ArrayUtilities.two_sum([2, 7, 11, 15], 9))
    print("Three Sum demo:", ArrayUtilities.three_sum([-1, 0, 1, 2, -1, -4]))
    print("Three Sum Closest demo:", ArrayUtilities.three_sum_closest([1, 2, 4, 5, 6], 10))