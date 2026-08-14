# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        queue = [root]
        addition = 0
        maxi = 0
        level = 1
        maxi_level = None
        upcoming = []
        while queue:
            length = len(queue)
            addition = 0
            for i in range(length):
                node = queue.pop(0)
                addition += node.val
                if node.left:
                    upcoming.append(node.left)
                if node.right:
                    upcoming.append(node.right)
            print("addition:",addition)
            if addition>maxi or maxi_level == None:
                maxi_level = level
                maxi= addition
            queue = upcoming
            upcoming = []  
            level +=1
        return maxi_level