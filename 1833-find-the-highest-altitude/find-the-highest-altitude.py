class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current = 0
        start = 0
        for i in gain:
            current += i
            if current > start:
                start = current
        return start
        