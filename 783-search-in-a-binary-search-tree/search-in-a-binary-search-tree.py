# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        res = None
        if root.val == val:
            # res.append(root)
            # res.append(root.left)
            # res.append(root.right)
            return root
        def traverse(root,val):
            if not root:
                return
            if root.val == val:
                # print("here it becomes true")
                # res.append(root)
                # res.append(root.left)
                # res.append(root.right)
                # print(root,root.left,root.right)
                # print(root)
                return root
            else:
                res = traverse(root.left,val)
                if res:
                    return res
                res = traverse(root.right,val)
                if res:
                    return res
        res = traverse(root.left,val)
        if res:
            print("Found in left:",res)
            return res
        res = traverse(root.right,val)
        if res:
            print("Found in right:",res)
            return res
        return res
        