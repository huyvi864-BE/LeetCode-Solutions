class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # if len(s) <= k:
        #     return s
        # cut = [s[i:i+k] for i in range(0, len(s), k)]
        # new = []
        # for j in cut:
        #     total = sum(int(ch) for ch in j)
        #     new.append(str(total))
        # res = ''.join(new)
        # return self.digitSum(res, k)

        while len(s) > k:
            new_s = ""
            for i in range(0, len(s), k):
                cut = s[i:i+k]
                total = sum(int(ch) for ch in cut)
                new_s += str(total)
            s = new_s
        return s