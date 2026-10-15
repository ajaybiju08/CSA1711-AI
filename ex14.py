import math

def minimax_alpha_beta(depth, node_index, is_maximizing, values, alpha, beta, target_depth):
    """
    Implements the Minimax algorithm with Alpha-Beta Pruning.
    
    Parameters:
    - depth: Current depth in the game tree.
    - node_index: Index of the current node in the leaf values array.
    - is_maximizing: True if the current layer is a Maximizing player, False if Minimizing.
    - values: List containing the scores of all leaf nodes.
    - alpha: The best alternative found so far for the Maximizing player (initialized to -infinity).
    - beta: The best alternative found so far for the Minimizing player (initialized to +infinity).
    - target_depth: The total depth of the tree where leaf values are located.
    """
    # Base case: target depth reached (leaf node)
    if depth == target_depth:
        return values[node_index]

    if is_maximizing:
        max_eval = -math.inf
        
        # Recur for left and right children (assuming a binary tree structure)
        for i in range(2):
            child_index = node_index * 2 + i
            eval_score = minimax_alpha_beta(
                depth + 1, child_index, False, values, alpha, beta, target_depth
            )
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            
            # Alpha-Beta Pruning condition
            if beta <= alpha:
                print(f"  [Pruned] Maximizer cut off remaining branches at depth {depth}")
                break
                
        return max_eval

    else:
        min_eval = math.inf
        
        # Recur for left and right children
        for i in range(2):
            child_index = node_index * 2 + i
            eval_score = minimax_alpha_beta(
                depth + 1, child_index, True, values, alpha, beta, target_depth
            )
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            
            # Alpha-Beta Pruning condition
            if beta <= alpha:
                print(f"  [Pruned] Minimizer cut off remaining branches at depth {depth}")
                break
                
        return min_eval


# Driver Code
if __name__ == "__main__":
    # Example tree with 8 leaf nodes (Perfect binary tree of depth 3)
    # Binary representation layout index-wise from left to right at depth 3
    leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]
    tree_depth = 3  # log2(8) = 3 layers deep

    print("Starting Alpha-Beta Pruning Search...")
    
    # Initialize alpha as -infinity and beta as +infinity
    initial_alpha = -math.inf
    initial_beta = math.inf
    
    optimal_value = minimax_alpha_beta(
        depth=0, 
        node_index=0, 
        is_maximizing=True, 
        values=leaf_values, 
        alpha=initial_alpha, 
        beta=initial_beta, 
        target_depth=tree_depth
    )
    
    print(f"\nThe optimal value for the root node is: {optimal_value}")
