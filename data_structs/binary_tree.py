# Binary tree:
# Every node has at most 2 child nodes
# Binary tree search complexity - every iteration we reduce search space by 1/2
# n = 8 -> 4 -> 2 -> 1 ->
# 3 iterations -> log2(8) = 3 -> search complexity = 0(log n)
# 2 search techniques: Breadth first search &  Depth First Search (In order traversal, pre order traversal, post order traversal)

# Depth first search (using recursion for every subtree search; always start with left subtree):
# In order - first fo to left subtree, then to root, then to right subtree
# Pre order - start with root, then go to left subtree, then go to right subtree
# Post order - start with left subtree, then go to right subtree, then to root

# Binary search tree - left side has all the elements that are less then the current node and the right side has all the elements that are greater then the current node

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:  # binary search cant have duplicate elements so need to check for that first
            return
        if data < self.data:
            # add data in left subtree
            if self.left:  # check first wether subtree has data
                # if it does, recursively add child to the element
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # ass always visit the left tree first
        if self.left:
            elements += self.left.in_order_traversal()  # if it has elements, extend list

        # visit base node
        elements.append(self.data)

        # visit the right tree first
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # value MIGHT BE in left subtree
            if self.left:
                # call the recursion and further go into left subtree
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # value MIGHT BE in left subtree
            if self.right:
                # call the recursion and further go into left subtree
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        node = self
        while node.left:
            node = node.left
        return node.data

    def find_max(self):
        node = self
        while node.right:
            node = node.right
        return node.data

    def calculate_sum(self):
        return sum(self.in_order_traversal())

    def post_order_traversal(self):
        elements = [self.data]

        # ass always visit the left tree first
        if self.left:
            elements += self.left.in_order_traversal()  # if it has elements, extend list

        # visit the right tree first
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        # ass always visit the left tree first
        if self.left:
            elements += self.left.in_order_traversal()  # if it has elements, extend list

        # visit the right tree first
        if self.right:
            elements += self.right.in_order_traversal()

        # visit base node
        elements.append(self.data)

        return elements


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


numbers = [23, 25, 43, 46, 2, 64, 1, 26, 76]
numbers_tree = build_tree(numbers)

# print(numbers_tree.in_order_traversal())
# gives back an ascending sorted list without any duplicates (sorter Set class)

# value = numbers_tree.search(64)

print(numbers_tree.find_min())
print(numbers_tree.find_max())
print(numbers_tree.calculate_sum())
print(numbers_tree.post_order_traversal())
print(numbers_tree.pre_order_traversal())
