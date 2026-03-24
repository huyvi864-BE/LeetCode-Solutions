class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        set_arr = set(arr)
        res = []
        count = 0
        for i in set_arr:
            count = arr.count(i)
            if count in res:
                return False
            res.append(count)
        return True




        