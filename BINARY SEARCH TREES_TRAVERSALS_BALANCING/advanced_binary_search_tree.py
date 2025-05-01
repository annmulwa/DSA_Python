class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(username = '{}', name = '{}', email = '{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


john = User('John Doe', 'johnd', 'john@example.com')
mary = User('Mary Smith', 'marys', 'mary@gmail.com')
paul = User('Paul Johnson', 'paulj', 'paul@hotmail.com')
lisa = User('Lisa Ray', 'lisar', 'lisa@yahoo.com')
alex = User('Alex Kim', 'alexk', 'alex@outlook.com')

users = [alex, john, lisa, mary, paul]

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

tree = BSTNode(mary.username, mary)
print(tree.key, tree.value)

tree.left = BSTNode(john.username, john)
tree.left.parent = tree
tree.right = BSTNode(paul.username, paul)
tree.right.parent = tree

print(tree.left.key, tree.left.value, tree.right.key, tree.right.value)

tree.left.left = BSTNode(alex.username, alex)
tree.left.left.parent = tree.left
tree.left.right = BSTNode(lisa.username, lisa)
tree.left.right.parent = tree.left

print(tree.left.left.key, tree.left.left.value, tree.left.right.key, tree.left.right.value)

def display_keys(node, space='\t', level=0):
    # print (node.key if node else None, level)

    # If the node is empty
    if node is None:
        print(space * level + '$')
        return

    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)

result = display_keys(tree, '        ')
print(result)

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

tree = insert(None, mary.username, mary)
print(tree.key, tree.value)
insert(tree, john.username, john)
insert(tree, paul.username, paul)
insert(tree, alex.username, alex)
insert(tree, lisa.username, lisa)
print(display_keys(tree))

tree1 = insert(None, alex.username, alex)
insert(tree1, john.username, john)
insert(tree1, lisa.username, lisa)
insert(tree1, mary.username, mary)
insert(tree1, paul.username, paul)
print(display_keys(tree1))

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

result = tree_height(tree1)
print(result)

def tree_nodes(node):
    if node is None:
        return 0
    return 1 + tree_nodes(node.left) + tree_nodes(node.right)

result = tree_nodes(tree1)
print(result)

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)
node = find(tree, 'tanya')
print((node.key, node.value) if node else None)

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

update(tree, 'Mary Smith', User(username = 'Mary Smith', name = 'mary', email = 'mary@gmail.com'))
node = find(tree, 'Mary Smith')
print(node.value)

# List all in sorted order(in-order traversal)
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)
print(list_all(tree))

# Determine if a binary tree is balanced
#  -> The left subtree is balanced
#  -> The right subtree is balanced
#  -> The difference between the heights of the left subtree and right subtree should not be more than 1
def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height

print(is_balanced(tree))
print(is_balanced(tree1))

# A balanced binary search tree
def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid - 1, root)
    root.right = make_balanced_bst(data, mid + 1, hi, root)

    return root

data = [(user.username, user) for user in users]
print(data)
tree = make_balanced_bst(data)
print(display_keys(tree))
print(is_balanced(tree))

# balance an unbalanced binary search tree
def balanced_bst(node):
    return make_balanced_bst(list_all(node))

tree = None
for user in users:
    tree = insert(tree, user.username, user)

print(display_keys(tree))

tree1 = balanced_bst(tree)
print(display_keys(tree1))

# Building a tree map for users(insert, find, update, list_all)
class TreeMap():
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balanced_bst(self.root)
        else:
            update(self.root, key, value)

    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return tree_nodes(self.root)

    def display(self):
        return display_keys(self.root)

print(users)
treemap = TreeMap()
print(treemap.root if treemap else None)
print(treemap.display() if treemap else '$')

# performing insertion
treemap['Alex Kim'] = alex
treemap['John Doe'] = john
treemap['Lisa Ray'] = lisa
treemap['Mary Smith'] = mary
treemap['Paul Johnson'] = paul

print(treemap.root)
print(treemap.display())

print(treemap['John Doe'])

print(len(treemap))

for key, value in treemap:
    print(key, value)

print(list(treemap))

treemap['Mary Smith'] = User(username = 'Mary Smith', name = 'marys', email = 'marys@gmail.com')

print(treemap['Mary Smith'])