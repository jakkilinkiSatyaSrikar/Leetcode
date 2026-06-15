# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        first_val = []
        second_val = []
        if (root1.left == None and root1.right == None) and (root2.left == None and root2.right == None):
            return root1.val == root2.val
        if root1.left == None and root1.right == None:
            first_val.append(root1.val)
        if root2.left == None and root2.right == None:
            second_val.append(root2.val)
        def root1_traverse(root1):
            if not root1:
                return
            if (not root1.left) and (not root1.right):
                first_val.append(root1.val)
                return
            root1_traverse(root1.left)
            root1_traverse(root1.right) 
        root1_traverse(root1.left)
        root1_traverse(root1.right)
        def root2_traverse(root2):
            if not root2:
                return
            if (not root2.left) and (not root2.right):
                second_val.append(root2.val)
                return
            root2_traverse(root2.left)
            root2_traverse(root2.right)    
        root2_traverse(root2.left)
        root2_traverse(root2.right)
        print(first_val)
        print(second_val) 
        return first_val == second_val