class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  # each elem instance of TreeNode class
        self.parent = None

    def add_child(self, child):
        child.parent = self  # current instance becomes a parent if a child is appended
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, up_to=None):

        spaces = " " * self.get_level() * 2
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        if self.children:  # if parent has children
            for child in self.children:
                if up_to and child.get_level() > up_to:
                    continue
                # recursively call this function for every child that is being called
                child.print_tree(up_to=up_to)


def build_product_tree():
    root = TreeNode(data="Electronics")

    laptop = TreeNode(data="Laptop")
    laptop.add_child(TreeNode(data="Mac"))
    laptop.add_child(TreeNode(data="ASUS"))
    laptop.add_child(TreeNode(data="HP"))

    cellphone = TreeNode(data="Cell Phones")
    cellphone.add_child(TreeNode(data="iPhone"))
    cellphone.add_child(TreeNode(data="Google Pixel"))
    cellphone.add_child(TreeNode(data="Xiaomi"))

    tv = TreeNode(data="TV")
    tv.add_child(TreeNode(data="Samsung"))
    tv.add_child(TreeNode(data="Sony"))
    tv.add_child(TreeNode(data="LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


root = build_product_tree()
# print(root.get_level())
root.print_tree(up_to=1)
