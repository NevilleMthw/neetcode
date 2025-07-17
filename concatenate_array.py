from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # New array should be 2 * nums,basically concatenated of two nums arrays

        ans = nums * 2

        return ans


# Time Complexity: O(n)
# Space Complexity: O(n)