from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumHash = {} # value : index {3:0, 4:1, 5:2, 6:3}

        # We need index and value
        for i, value in enumerate(nums):
            difference_value = target - value # 7 - 3 = 4
            if difference_value not in sumHash:
                # If diff not in the hash map, we add the value and the index from the array
                sumHash[value] = i # value : index is added to hashmap
            else:
                # If in hashmap, just return the indices
                # sumHash[difference_value] returns index 0 because difference_value is 3,
                # and it uses 3 as the value to search in the hash map so it gets 0 index back
                return [sumHash[difference_value], i]

solution = Solution()
solution.twoSum(nums=[3, 4, 5, 6], target=7)

# Time and space: O(n)