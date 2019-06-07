# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#Hardcoding by dfs
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        x=[]
        y= []
        def findLeaf(root,a):
            if not root: return
            findLeaf(root.left,a)
            if not root.left and not root.right:
                a.append(root.val)
            findLeaf(root.right,a)
            return a
        x=findLeaf(root1,x)
        y=findLeaf(root2,y)
        if x==y:
            return True
        else:
            return False
            
      
           
                
            
        
