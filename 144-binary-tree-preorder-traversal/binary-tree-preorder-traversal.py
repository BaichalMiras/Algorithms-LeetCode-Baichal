# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = [] #cписок для значений узлов
        
        def visit_node(node):
            if not node:
                return
            #узел > лево > право
            result.append(node.val)
            visit_node(node.left)
            visit_node(node.right)
            
        visit_node(root)
        return result