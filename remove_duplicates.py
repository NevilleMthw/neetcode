class Solution:
    # Not using two pointers - not optimal
    def removeDuplicates(self, nums: list[int]) -> int:

        # Basically takes all the elements from the list, sorts it and converts to a set
        # By default set() does not keep duplicates
        nums[:] = sorted(set(nums))

        print(nums)
        return print(int(len(nums)))

solution = Solution()
solution.removeDuplicates([2,10,10,30,30,30])