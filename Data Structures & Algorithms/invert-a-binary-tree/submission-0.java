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
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return null;
        invertNode(root);
        return root;
    }

    public void invertNode(TreeNode node) {
        //If this is a leaf node, return the node itself
        if(node.left == null && node.right == null) {
            return;
        } else {
            //Invert the node
            TreeNode lft = node.left;
            node.left = node.right;
            node.right = lft;
        }
        
        if(node.left != null) invertNode(node.left);
        if(node.right != null) invertNode(node.right);
    }
}
