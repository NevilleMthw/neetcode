from typing import List

# Not using two pointers - not optimal
class Solution:
    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:
        # Removing from an array is a O(n) operation
        # To modify the array in-place, not create a new array

        k = 0
        # Iterate over all the indexes instead of the values in the list
        for i in reversed(range(len(nums))):
            # If nums contains val, remove/pop
            if nums[i] == val:
                nums.pop(i)
            k += 1


        return k

solution = Solution()
solution.remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2)