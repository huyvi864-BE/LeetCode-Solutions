class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        result = []
        current = 1
        for num in target:
            while current < num:
                result.append("Push")
                result.append("Pop")
                current += 1
            result.append("Push")
            current += 1
        return result