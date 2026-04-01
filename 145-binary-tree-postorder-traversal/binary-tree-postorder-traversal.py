# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []  #список для значений узлов
        
        def visit_node(node):
            if not node:
                return
            #лево > право > узел
            visit_node(node.left)
            visit_node(node.right)
            result.append(node.val)
            
        visit_node(root)
        return result