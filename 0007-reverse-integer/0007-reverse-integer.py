class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2**31-1
        int_min = -2**31
        if x == int_min:
            return 0
        dau = -1 if x < 0 else 1
        x = abs(x)
        rever = 0
        
        while x > 0:
            so_cuoi = x%10
            x //= 10

            if rever > int_max // 10 or (rever == int_max //10 and so_cuoi >7):
                return 0
            rever = rever * 10 +so_cuoi
        return rever * dau
        