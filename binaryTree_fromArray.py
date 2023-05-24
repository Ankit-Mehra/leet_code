"""Given an array that represents a tree in such a way that array indexes are values in tree nodes 
and array values give the parent node of that particular index (or node). The value of the root 
node index would always be -1 as there is no parent for root. Construct the standard linked 
representation of given Binary Tree from this given representation."""


class Node:
    def __init__(self,root=None,left=None,right=None):
        self.root = root
        self.left = left
        self.right = right

def tree_fromArray(arr:list[int])->list:
    out = []
    j = item = -1
    while len(out) < len(arr):
        i = 0
        while i < len(arr):
            if arr[i] == item:
                out.append(i)
            i+=1
        j+=1
        item = out[j]
    return out

print(tree_fromArray([-1,0,0,1,1,3,5]))