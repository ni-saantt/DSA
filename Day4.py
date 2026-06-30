# Day4 - Even number utilities.

"""
Utilities for handling even numbers in a list.
"""

class EvenCounter:
    """Provides methods to filter even numbers and count them."""

    @staticmethod
    def get_evens(nums: list[int]) -> list[int]:
        """Return a list of even numbers from the input list."""
        return [num for num in nums if num % 2 == 0]

    @staticmethod
    def count_evens(nums: list[int]) -> int:
        """Return the count of even numbers in the input list."""
        return len(EvenCounter.get_evens(nums))

if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    evens = EvenCounter.get_evens(numbers)
    print("Evens:", evens)
    print("Count:", EvenCounter.count_evens(numbers))
