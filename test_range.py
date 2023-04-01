import range_search as rs

def is_bst(node: rs.BST_node, lower=float('-inf'), upper=float('inf')):
    """Tests if a tree is a binary search tree."""
    if node is None: # check if we have reached an empty node
        return True

    key = node.key
    if key <= lower or key >= upper: # check violating conditions
        return False

    if not is_bst(node.left, lower, key): # explore left subtree
        return False

    if not is_bst(node.right, key, upper): # explore right subtree
        return False

    return True

def corrupt_bst(node: rs.BST_node, ratio: float 0.1):
    """Function to randomly corrupt a portion of the data in a BST."""
 
bst = rs.BST()
print(is_bst(bst.root))
bst.insert(64,"Pyrénées-Atlantique")
bst.insert(81,"Tarn")
bst.insert(75,"Paris")
bst.insert(33,"Gironde")
bst.insert(31,"Haute-Garonne")
bst.insert(3,"Allier")
bst.insert(2,"Aisne")
nodes_found = bst.range_search(21,77)
for n in nodes_found:
    print(n)

# corrupt binary search tree

