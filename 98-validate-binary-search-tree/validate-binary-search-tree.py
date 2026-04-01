# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, min_v, max_v):
            #если дошли до пустого узла, значит на этом пути ошибок нет
            if not node:
                return True
            
            #проверяем нижнюю границу, если она задана
            if min_v is not None and node.val <= min_v:
                return False
            
            #проверяем верхнюю границу, если она задана
            if max_v is not None and node.val >= max_v:
                return False
            
            #рекурсивно идем вниз:
            #для левого узла текущий узел становится верхней границей
            #для правого узла текущий узел становится нижней границей
            return validate(node.left, min_v, node.val) and \
                   validate(node.right, node.val, max_v)

        return validate(root, None, None)