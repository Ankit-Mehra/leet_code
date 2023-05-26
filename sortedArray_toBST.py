
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def inorder_traversal(root)->list:
    traverse = []
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        traverse.append(root.val)
        root = root.right
    return traverse

def sortedArrayToBST(nums: list[int]) -> TreeNode:
    node = TreeNode()
    if len(nums) <= 2 :
        node.val = nums[-1]
        node.left = nums[0]
        return node

    median = len(nums)//2
    node.val = nums[median]
    median += 1
    node.right = TreeNode(nums[median])
    node.left = TreeNode(nums[-(median+1)])
    temp1 = node.left
    temp2 = node.right
    median += 1
    while median < len(nums):
        temp1.left = TreeNode(nums[-(median + 1)])
        temp2.right = TreeNode(nums[median])
        temp1 = temp1.left
        temp2 = temp2.right
        median += 1
    return node

def sortedArrayToBST1(nums: list[int]) -> TreeNode:
    if len(nums) == 0:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST1(nums[:mid])
    root.right = sortedArrayToBST1(nums[mid+1:])
    return root

temp = [-10,-3,0,5,9]
node = sortedArrayToBST1(temp)
print(inorder_traversal(node))
