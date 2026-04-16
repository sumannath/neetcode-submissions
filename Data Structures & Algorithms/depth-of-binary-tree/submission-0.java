/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null) return 0;
        
        return traverse(root);
    }
    
    public int traverse(TreeNode node) {
        if(node.left == null && node.right == null) {
            return 1;
        } else {
            int leftDepth = 0, rightDepth = 0;
            if(node.left != null) leftDepth = traverse(node.left);
            if(node.right != null) rightDepth = traverse(node.right);

            return 1 + Math.max(leftDepth, rightDepth);        
        }
    }
}
