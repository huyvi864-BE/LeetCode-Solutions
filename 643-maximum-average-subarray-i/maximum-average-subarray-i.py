class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        max_sum = float('-inf')
        for i in range(n - k + 1):
            current_sum = prefix[i + k] - prefix[i]
            if current_sum > max_sum:
                max_sum = current_sum
        return float(max_sum) / k


        