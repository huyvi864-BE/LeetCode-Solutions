class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result = []
        for token in tokens:
            if token[-1].isdigit():
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
                else:
                    result.append(int(float(a) / b))
        return  result[0]