# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_val):
            if not node:
                return 0
            
            good = 1 if node.val >= max_val else 0
            
            current_max = max(max_val, node.val)
        
            good += dfs(node.left, current_max)
            good += dfs(node.right, current_max)
            
            return good
            
        return dfs(root, root.val)
        