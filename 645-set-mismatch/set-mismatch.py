class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        s = sum(set(nums))
        return [sum(nums) - s, n * (n + 1) // 2 - s]