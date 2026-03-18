class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_set = set('aeiouAEIOU')
        stack = []
        for char in s:
            if char in vowels_set:
                stack.append(char)
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] in vowels_set:
                s_list[i] = stack.pop()              
        return "".join(s_list)