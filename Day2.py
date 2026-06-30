# Day2 - Number processing utilities.

"""
Day2 - Number processing utilities.
"""

class NumberProcessor:
    """Encapsulates various number processing operations."""

    @staticmethod
    def find_largest(nums: list[int]) -> int:
        """Return the largest number in the list."""
        if not nums:
            raise ValueError("Empty list provided")
        largest = nums[0]
        for nu in nums[1:]:
            if nu > largest:
                largest = nu
        return largest

    @staticmethod
    def print_numbers(nums: list[int]) -> None:
        """Print each number in the list."""
        for num in nums:
            print(num)

    @staticmethod
    def even_numbers(nums: list[int]) -> tuple[list[int], int]:
        """Return a list of even numbers and their count."""
        evens = [num for num in nums if num % 2 == 0]
        for ev in evens:
            print(ev)
        return evens, len(evens)

if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Largest:", NumberProcessor.find_largest(numbers))
    print("All numbers:")
    NumberProcessor.print_numbers(numbers)
    evens, count = NumberProcessor.even_numbers(numbers)
    print("Count of evens:", count)
