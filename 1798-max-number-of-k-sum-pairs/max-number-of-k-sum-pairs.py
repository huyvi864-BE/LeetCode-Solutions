import math 
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        res = 0
        for num in nums:
            complement = k - num
            if dic.get(complement, 0) >0:
                res +=1
                dic[complement] -= 1
            else:
                dic[num] = dic.get(num, 0) + 1
        return res


