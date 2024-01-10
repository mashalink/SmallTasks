/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool compare_trees(int *tree_1, int *tree_2, int index_1){
    int index = 0;

    while (index < index_1)
    {
        if (tree_1[index] != tree_2[index])
            return (false);
        index++;
    }
    return (true);
}

void searce_value_sequence(struct TreeNode* root, int *sequence, int *index){

    if (!root->left && !root->right)
    {
        sequence[*index] = root->val;
            *index = *index + 1;
        return ;
    }
    else 
    {
        if (root->left)
            searce_value_sequence(root->left, sequence, index);
        if (root->right)
            searce_value_sequence(root->right, sequence, index);
    }
    return ;
} 

bool leafSimilar(struct TreeNode* root1, struct TreeNode* root2) {
    int tree_1[100];
    int tree_2[100];
    int index_1 = 0;
    int index_2 = 0;

    searce_value_sequence(root1, tree_1, &index_1);
    searce_value_sequence(root2, tree_2, &index_2);
    if (index_1 == index_2)
        return (compare_trees(tree_1, tree_2, index_1));
    return (false);
}
