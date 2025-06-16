class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# node0 = TreeNode(2)
# node1 = TreeNode(3)
# node2 = TreeNode(5)
# node3 = TreeNode(1)
# node4 = TreeNode(3)
# node5 = TreeNode(7)
# node6 = TreeNode(4)
# node7 = TreeNode(6)
# node8 = TreeNode(8)

# node0.left = node1
# node0.right = node2

# node1.left = node3

# node2.left = node4
# node2.right = node5

# node4.right = node6

# node5.left = node7
# node5.right = node8

# tree = node0

# print(node5.right.key)

# tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6,7,8)))

def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6,7,8))))

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

result = display_keys(tree2, '   ')
print(result)

def traverse_in_order(node):
    if node is None:
        return []
    return(traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

result = traverse_in_order(tree2)
print(result)

def traverse_pre_order(node):
    if node is None:
        return []
    return([node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right))

result = traverse_pre_order(tree2)
print(result)

def traverse_post_order(node):
    if node is None:
        return []
    return(traverse_post_order(node.left) + traverse_post_order(node.right) + [node.key])

result = traverse_post_order(tree2)
print(result)

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

result = tree_height(tree2)
print(result)

def tree_nodes(node):
    if node is None:
        return 0
    return 1 + tree_nodes(node.left) + tree_nodes(node.right)

result = tree_nodes(tree2)
print(result)

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and
                    (max_l is None or node.key > max_l) and
                    (min_r is None or node.key < min_r))

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    return is_bst_node, min_key, max_key

result = is_bst(tree2)
print(result)
