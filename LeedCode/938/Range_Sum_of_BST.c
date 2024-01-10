/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int check_the_number_in_the_range(int number, int low, int high){
    if (number >= low && number <= high)
        return (1);
    return (0);
}

int next_step(struct TreeNode* left, struct TreeNode*  right, int low, int high){
    int sum = 0;

    if (right != NULL)
    {
        if (check_the_number_in_the_range(right->val, low, high)){
            sum += right->val;
        }
        sum += next_step(right->left, right->right, low, high);
    }
    if (left != NULL)
    {
        if (check_the_number_in_the_range(left->val, low, high)){
            sum += left->val;
        }
        sum += next_step(left->left, left->right, low, high);
    }
    return (sum);
} 

int rangeSumBST(struct TreeNode* root, int low, int high) {
    int sum = 0;

    if (check_the_number_in_the_range(root->val, low, high))
        sum += root->val;
    sum += next_step(root->left, root->right, low, high);
    return (sum);
}