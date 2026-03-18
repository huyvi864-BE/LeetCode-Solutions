class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        jump = 0
        while jump < len(flowerbed) and n >0:
            if flowerbed[jump] == 1:
                jump += 2
            elif jump == len(flowerbed) - 1 or flowerbed[jump+ 1] == 0:
                n -= 1
                jump +=2
            else:
                jump +=3
        return n <= 0
            

        