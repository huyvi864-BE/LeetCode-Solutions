class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum =0
        current =0
        for num in nums:
            if num ==1:
                current +=1
            else:
                maximum = max(maximum,current)
                current =0
        return max(maximum,current)

            
