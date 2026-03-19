class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] *n
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
        right = 1
        for s in range(n-1,-1,-1):
            res[s] *= right
            right *= nums[s]
        return res
        

                

        