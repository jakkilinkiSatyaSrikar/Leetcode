# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = []
        queue.append(root)
        upcoming = []
        res=[]
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if node.left: upcoming.append(node.left)
                if node.right: upcoming.append(node.right)
                # print("upcoming",upcoming,end="\n")
                if i == length-1:
                    res.append(node.val)
                    print(res)
            queue = upcoming
            upcoming = []
        return res