# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def deleteNode(self, node_root, key_value):
        """
        :type node_root: Optional[TreeNode]
        :type key_value: int
        :rtype: Optional[TreeNode]
        """
        
        if not node_root:
            return None
        
        if key_value < node_root.val:
            #если значение меньше текущего узла,то идём в левое поддерево
            node_root.left = self.deleteNode(node_root.left, key_value)

        elif key_value > node_root.val:
            #если значение больше текущего узла, то идём в правое поддерево
            node_root.right = self.deleteNode(node_root.right, key_value)

        else:
            #нашли узел, который нужно удалить
            
            #нет левого поддерева
            if not node_root.left:
                return node_root.right
            
            #нет правого поддерева
            if not node_root.right:
                return node_root.left
            
            #два ребёнка
            smallest = node_root.right
            while smallest.left:
                smallest = smallest.left
            
            node_root.val = smallest.val
            node_root.right = self.deleteNode(node_root.right, smallest.val)
        
        return node_root