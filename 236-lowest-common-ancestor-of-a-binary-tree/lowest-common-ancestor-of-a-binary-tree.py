# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        li = [p,q]
        if root.left in li and root.right in li:
            return root
        if root in li or root in li:
            return root
        def LCA(root,p,q):
            if not root:
                return
            if root == p:
                return p
            elif root == q:
                return q
            else:
                if root.left and root.right:
                    r1 = LCA(root.left,p,q)
                    r2 = LCA(root.right,p,q)
                    if r1 and r2:
                        return root
                    elif r1:
                        return r1
                    elif r2:
                        return r2
                    else:
                        return
                elif root.left and (not root.right):
                    r = LCA(root.left,p,q)
                    print(r)
                    if r:
                        return r
                elif ((not root.left) and root.right):
                    r = LCA(root.right,p,q)
                    print(r)
                    if r:
                        return r
                else:
                    return 
        r1 = LCA(root.left,p,q)
        r2 = LCA(root.right,p,q)
        print("r1:\n",r1,"\n")
        print("r2:\n",r2,"\n")
        if r1 and r2:
            return root
        elif r1:
            return r1
        elif r2:
            return r2
        else:
            return None