class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        counts1 = sorted(Counter(word1).values())
        counts2 = sorted(Counter(word2).values())
        
        return counts1 == counts2
        