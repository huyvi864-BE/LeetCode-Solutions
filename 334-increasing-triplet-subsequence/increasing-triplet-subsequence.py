class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = 2**31 -1
        second = 2**31 -1
        for num in nums:
            if num <= first :
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False