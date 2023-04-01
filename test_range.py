# stdlib modules
import argparse
import random
import string

# custom modules
import range_search as rs

# instantiate argument parser
parser = argparse.ArgumentParser(description="Test Hash BST range search")
parser.add_argument("-m", default=10, type=int,
                    help="Number of tree nodes")
parser.add_argument("-n", default=5, type=int,
                    help="Lenght of record strings")
args = parser.parse_args()

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

def corrupt_bst(node: rs.BST_node, ratio: float = 0.5):
    """Function to randomly corrupt a portion of the data in a BST."""
    if node is not None:
        change = True if random.random() < ratio else False
        if change:
            node.key = random.choice(range(100))
        # explore left subtree
        corrupt_bst(node.left, ratio)
        # explore right subtree
        corrupt_bst(node.right, ratio) 

print("(*) Creating empty BST.")
bst = rs.BST()
print(f"(*) Is it a BST?: {is_bst(bst.root)}\n")

m, n = args.m, args.n
# create a list of random nodes to insert
rand_keys = random.sample(range(100), m)
chars = string.ascii_letters + string.digits
rand_strs = [''.join(random.choice(chars) for _ in range(n)) for _ in range(m)]
for key, string in zip(rand_keys, rand_strs):
    print(f"Inserting ({key}, {string})")
    bst.insert(key, string)

print(f"\n(*) Search results for keys in range [21, 77]:")
nodes_found = bst.range_search(21,77)
for n in nodes_found:
    print(n)

print("\n(*) Corrupting binary tree")
# corrupt binary search tree
corrupt_bst(bst.root)
print(f"(*) Is it a BST?: {is_bst(bst.root)}")
