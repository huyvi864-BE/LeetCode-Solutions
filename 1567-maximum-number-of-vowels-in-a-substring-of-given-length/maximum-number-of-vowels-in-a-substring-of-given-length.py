class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        letter = set("aeiou")
        curent = 0
        for i in range(k):
            if s[i] in letter:
                curent += 1
        max_letter = curent
        for i in range(k, len(s)):
            if s[i] in letter:
                curent += 1
            if s[i - k] in letter:
                curent -= 1
            if curent > max_letter:
                max_letter= curent 
            if max_letter == k:
                return k
        return max_letter        