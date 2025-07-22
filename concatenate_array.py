from typing import List


class Solution:
    # Not optimal since not using iteration, one or two pass method
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # New array should be 2 * nums,basically concatenated of two nums arrays

        ans = nums * 2

        return ans


# Time Complexity: O(n)
# Space Complexity: O(n)