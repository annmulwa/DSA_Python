# BRUTE FORCE SOLUTION
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

users = [john, mary, paul, lisa, alex]
# print(users)

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def find_all(self):
        return self.users

database = UserDatabase()

database.insert(john)
database.insert(mary)
database.insert(paul)
database.insert(alex)

database.update(User(username = 'Mary Smith', name = 'marysmith', email = 'mary@gmail.com'))

user = database.find('Mary Smith')
# print(user)

# allusers = database.find_all()
# print(allusers)

# BINARY SEARCH TREE SOLUTION

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

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

tree = parse_tuple((('alex','john','lisa'), 'mary', 'paul'))
print(tree)

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

result = display_keys(tree, '      ')
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

result = is_bst(tree)
print(result)
