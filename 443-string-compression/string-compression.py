class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars: return 0
        res = ""
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                res += chars[i-1]
                if count > 1:
                    res += str(count)
                count = 1 
        res += chars[-1]
        if count > 1:
            res += str(count)
        for i in range(len(res)):
            chars[i] = res[i]
            
        return len(res)