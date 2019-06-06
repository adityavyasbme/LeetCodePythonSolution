def check_binary_search_tree_(root):
    def helper(node,lower=float('-inf'),upper=float('inf')):
        if not node:
            return True
        val = node.data
        if val <= lower or val >= upper:
            return False

        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True

    return helper(root)


def check_binary_search_tree_(root):
    if not root: return None
    stack = [(root,float('-inf'),float('inf'))]
    while stack:
        root,lower,upper=stack.pop()
        if not root: continue
        data = root.data
        if data<=lower or data>=upper:
            return False
        stack.append((root.right,data,upper))
        stack.append((root.left,lower,data))
    return True




