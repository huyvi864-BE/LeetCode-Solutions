class Solution:
    def canAliceWin(self, n: int) -> bool:
        a =10
        turn = True 
        for i in range(n):
            if n >= a:
                n -=a
                a -= 1
                turn = not turn
        return not turn 



        