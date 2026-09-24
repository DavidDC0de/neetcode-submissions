# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        current = [root]

        while current:
            values = []
            depth = []

            for node in current:
                values.append(node.val)

                if node.left:
                    depth.append(node.left)

                if node.right:
                    depth.append(node.right)

            res.append(values)
            current = depth
        return res

        