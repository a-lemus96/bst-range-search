# Node class
class BST_node:
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return "(key=" + str(self.key) + ",data=" + str(self.data) + ")"

# Tree class
class BST:
    def __init__(self):
        # Empty tree, initially
        self.root = None

    def __range_search(self, node, keymin,keymax):
        node_list = []
        if node.key >= keymin:
            if node.left != None:
                # Search in the left tree
                node_list = node_list + self.__range_search(node.left, keymin, keymax)

        # Check if we need to add the current node
        if node.key <= keymax and node.key >= keymin:
            node_list.append(node)

        if node.key<=keymax:
            if node.right != None:
                # Search in the right tree
                node_list = node_list + self.__range_search(node.right, keymin, keymax)
        return node_list

    # Main search method
    def range_search(self, keymin, keymax):
        return self.__range_search(self.root, keymin,keymax)

    # Insert a (key,data) pair
    def insert(self, key, data):
        new_node = BST_node(key,data)
        parent = None
        node = self.root
        # Explore the tree until finding a leaf where we can introduce our data
        # We need to keep track of the parent node
        while node!=None:
            parent = node
            if new_node.key < node.key:
                node = node.left
            else:
                node = node.right
        # Check the parent of x
        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
