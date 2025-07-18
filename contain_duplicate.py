from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # If duplicates in duplicateHash then return True else it will
        # add to the duplicateHash and then go through the loop again
        # to check if there is a duplicate or not
        # So if the value is added in then it will check again and see if it is a duplicate or not

        duplicateHash = {}

        for duplicates in nums:
            if duplicates in duplicateHash:
                return True
            else:
                duplicateHash[duplicates] = 1

        return False

# Time complexity: O(n)
# Space complexity: O(n)


solution = Solution()
# solution.hasDuplicate([1,1,2])
solution.hasDuplicate([1,2,3])