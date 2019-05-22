#using DFS
class Solution:
    def rangeSumBST(self, root, L, R):
        def dfs(root):
            if not root:
                return
            if L <= root.val <= R:
                self.res += root.val
            if L <= root.val:
                dfs(root.left)
            if R >= root.val:
                dfs(root.right)
        self.res = 0
        dfs(root)
        return self.res
#Runtime 248
#Using simple recursion
class Solution:
    def rangeSumBST(self, root, L, R):
        if not root: return 0
        l = self.rangeSumBST(root.left, L, R)
        r = self.rangeSumBST(root.right, L, R)
        return l + r + (L <= root.val <= R) * root.val
     
