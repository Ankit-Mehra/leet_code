"""Given the root of a binary tree, check whether it is a
 mirror of itself (i.e., symmetric around its center)."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root:TreeNode) -> bool:
        
        def recur(root_left,root_right):
            symmetry = True
            if root_left.left.val == root_right.right.val and root_left.right.val == root_right.left.val:
                return symmetry
            else:
                symmetry = False
                return symmetry

            while root_left or root_right:
                return recur(root_left.left,root_right.right) == recur(root_left.right,root_right.left)
        
        return recur(root.left,root.right)
def isSymmetric2(root: TreeNode) -> bool:
        
        def recur(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return root1.val == root2.val and recur(root1.right,root2.left) and recur(root1.left,root2.right)
        
        return recur(root,root)

print(max(4,5))

sym_tree = TreeNode(1)
sym_tree.left = TreeNode(2)
sym_tree.right = TreeNode(2)
sym_tree.left.left = TreeNode(3)
sym_tree.left.right = TreeNode(3)
sym_tree.right.left = TreeNode(4)
sym_tree.right.right = TreeNode(3) 


print(isSymmetric(sym_tree))
print(isSymmetric2(sym_tree))