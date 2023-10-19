class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


depths_arr = []


def sum_of_depths(root: TreeNode):
    depth_counter(root, 0)
    sum_dep = 0
    for i in range(len(depths_arr)):
        sum_dep += depths_arr[i]
    depths_arr.clear()
    return sum_dep


def depth_counter(node: TreeNode, depth: int):
    depths_arr.append(depth)
    if node.left is not None:
        depth_counter(node.left, depth + 1)
    if node.right is not None:
        depth_counter(node.right, depth + 1)

