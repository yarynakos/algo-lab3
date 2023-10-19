import unittest
from main import TreeNode, sum_of_depths


class TestSumOfDepths(unittest.TestCase):
    def test_sum_of_depths(self):
        root1 = TreeNode(1, TreeNode(0), TreeNode(3, TreeNode(2), TreeNode(5)))
        self.assertEqual(6, sum_of_depths(root1))  # 0 + 1 + 1 + 2 + 2 = 6

        root2 = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(8)), TreeNode(15))
        self.assertEqual(6, sum_of_depths(root2))  # 0 + 1 + 1 + 2 + 2 + 2 = 8

        root3 = TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5)))))
        self.assertEqual(10, sum_of_depths(root3))  # 0 + 1 + 2 + 3 + 4 = 10
