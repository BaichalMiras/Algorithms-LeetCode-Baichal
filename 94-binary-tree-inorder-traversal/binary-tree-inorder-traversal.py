# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        answer = []
        
        def traverse(current):
            if not current:
                return
            traverse(current.left)
            answer.append(current.val)
            traverse(current.right)
        
        traverse(root)
        return answer
        