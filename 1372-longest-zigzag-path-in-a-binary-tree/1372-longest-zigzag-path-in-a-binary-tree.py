# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_length = 0
        def dfs(node, go_left, steps):
            if not node:
                return
            

            self.max_length = max(self.max_length, steps)
            
            if go_left:
                dfs(node.left, False, steps + 1)
                
                dfs(node.right, True, 1)
            else:
                dfs(node.right, True, steps + 1)
                
                dfs(node.left, False, 1)

        dfs(root, True, 0)
        dfs(root, False, 0)
        
        return self.max_length
        