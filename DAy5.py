# DAy5 - Demo script with hashtags and a simple class.

"""
This module demonstrates a simple placeholder class.
"""

# --- Section: Imports ---
# (no external imports needed)

# --- Section: Demo Class ---
class Demo:
    """A simple demo class with a method to process a list and remove duplicates.
    It mirrors the original script functionality but is encapsulated.
    """

    @staticmethod
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
    result = Demo.remove_duplicates(nums)
    print("Deduped list:", result)
