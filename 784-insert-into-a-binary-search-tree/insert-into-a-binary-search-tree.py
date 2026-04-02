# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def insertIntoBST(self, start, value):
        """
        :type start: Optional[TreeNode]
        :type value: int
        :rtype: Optional[TreeNode]
        """
        
        if not start:
            return TreeNode(value)  #создаём новый узел
        
        if value < start.val:
            start.left = self.insertIntoBST(start.left, value)   #идем влево
        else:
            start.right = self.insertIntoBST(start.right, value) #идем вправо
        
        return start