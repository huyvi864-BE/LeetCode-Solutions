class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                result.append(int(token))
            else:
                b = result.pop()
                a = result.pop() 
                if token == '+':
                    result.append(a + b)
                elif token == '-':
                    result.append(a - b)
                elif token == '*':
                    result.append(a * b)
                elif token == '/':
                    result.append(int(float(a) / b))
        return result[0]