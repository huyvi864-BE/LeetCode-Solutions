class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        word = ""
        for char in s:
            if char != " ":
                word += char
            elif word != "":
                res.append(word)
                word = ""
        if word != "":
            res.append(word)
        res.reverse()
        return " ".join(res)             

        