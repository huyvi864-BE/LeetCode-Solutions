class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        total_pairs = 0
        
        for r in range(n):
            for c in range(n):
                is_match = True
                for i in range(n):
                    if grid[r][i] != grid[i][c]:
                        is_match = False
                        break
                if is_match:
                    total_pairs += 1
                    
        return total_pairs
        