"""Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


def maxDepth(root:TreeNode) -> int:
      if not root:
            return 0
      if not root.left and root.right:
            return 1
      return max(1+maxDepth(root.left),1+maxDepth(root.right))


sym_tree = TreeNode(1)
sym_tree.left = TreeNode(2)
sym_tree.right = TreeNode(2)
sym_tree.left.left = TreeNode(3)
sym_tree.left.right = TreeNode(3)
sym_tree.right.left = TreeNode(4)
sym_tree.right.right = TreeNode(3)
sym_tree.right.right.right = TreeNode(5)


print(maxDepth(sym_tree))