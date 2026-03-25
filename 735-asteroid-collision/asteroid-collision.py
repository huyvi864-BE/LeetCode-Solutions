class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                if stack[-1] < -ast:
                    stack.pop()
                    continue 
                elif stack[-1] == -ast:
                    stack.pop()
                break
            else:
                stack.append(ast)
                
        return stack
        