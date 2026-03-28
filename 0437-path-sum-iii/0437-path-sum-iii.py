# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.total_paths = 0
        
        prefix_sum_count = {0: 1}
        
        def dfs(node, current_sum):
            if not node:
                return
            
            current_sum += node.val
    
            if current_sum - targetSum in prefix_sum_count:
                self.total_paths += prefix_sum_count[current_sum - targetSum]
            
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
            
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            prefix_sum_count[current_sum] -= 1
            
        dfs(root, 0)
        return self.total_paths
        