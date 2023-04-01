# Binary Search Trees for 1D Range Search
This repository contains an implementation of a Binary Search Tree (BST) for performing 1-dimensional range search and display the results in ascending order with respect to the key values of each found node. It also includes an implementation of a function to test wheter a given tree is a BST.

### Running tests for 1D range search using a BST
---
The script `test_range.py` contains tests cases for evaluating the correctness of the search. Simply run `python test_range.py -m=M -n=N` being M the number of random nodes to insert into the tree and N the number of random character for each data associated to each node's key. The script performs the following actions:

1. Creates an empty BST ant tests if it is a BST using the `is_bst` function.
2. Inserts `M` nodes with random keys from the interval `[0, 99]` and random 5-character random strings as data.
3. Search and displays nodes with keys from within the interval `[21, 77]` in increasing order.
4. Corrupts binary tree by traversing it and assigning a random key to 50% of its nodes to enforce BST constraints violation.
5. Test if it is still being a binary tree after corruption.

Here is a screenshot of how the output might look like:

![image](https://user-images.githubusercontent.com/95151624/229263673-ece4da2f-d177-4b39-85d5-f9722abeb24a.png)
