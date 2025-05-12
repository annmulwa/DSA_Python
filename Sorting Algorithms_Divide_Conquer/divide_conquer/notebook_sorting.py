# Arranging notebooks according to decreasing number of likes

# function to capture basic information about notebooks
class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)

nb0 = Notebook("Python Basics", "alice", 120)
nb1 = Notebook("Advanced Machine Learning", "alice", 85)
nb2 = Notebook("Data Analysis with Pandas", "carol", 200)
nb3 = Notebook("Intro to SQL", "dave", 50)
nb4 = Notebook("Deep Learning Essentials", "eve", 300)
nb5 = Notebook("Statistics for Data Science", "frank", 110)
nb6 = Notebook("Natural Language Processing", "grace", 250)
nb7 = Notebook("Big Data with Spark", "heidi", 95)
nb8 = Notebook("Computer Vision Basics", "ivan", 180)
nb9 = Notebook("Time Series Analysis", "judy", 60)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]

# print(notebooks)

def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'

def default_compare(x, y):
    if x < y:
        return 'lesser'
    elif x == y:
        return 'equal'
    else:
        return 'greater'

# Implementing merge sort
def merge_sort(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(merge_sort(objs[:mid], compare), merge_sort(objs[mid:], compare), compare)

def merge(left, right, compare):
    i, j, merged = 0, 0, []

    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

sorted_notebooks = merge_sort(notebooks, compare_likes)
# print(sorted_notebooks)

def compare_titles(nb1, nb2):
    if nb1.title < nb2.title:
        return 'lesser'
    elif nb1.title == nb2.title:
        return 'equal'
    else:
        return 'greater'

sorted_notebooks = merge_sort(notebooks, compare_titles)
# print(sorted_notebooks)

def compare_usernames(nb1, nb2):
    if nb1.username < nb2.username:
        return 'lesser'
    elif nb1.username == nb2.username:
        if nb1.title < nb2.title:
            return 'lesser'
        elif nb1.title > nb2.title:
            return 'greater'
        return 'equal'
    else:
        return 'greater'

sorted_notebooks = merge_sort(notebooks, compare_usernames)
# print(sorted_notebooks)

# Implementing quick sort
def quick_sort(objs, start=0, end=None, compare=default_compare):
    if end is None:
        end = len(objs) - 1

    if start < end:
        pivot = partition(objs, start, end, compare)
        quick_sort(objs, start, pivot - 1, compare)
        quick_sort(objs, pivot + 1, end, compare)

    return objs

def partition(objs, start=0, end=None, compare=default_compare):
    if end is None:
        end = len(objs) - 1

    l, r = start, end - 1

    while l < r:
        left_result = compare(objs[l], objs[end])
        right_result = compare(objs[r], objs[end])
        if left_result == 'lesser' or left_result == 'equal':
            l += 1
        elif right_result == 'greater':
            r -= 1
        else:
            objs[l], objs[r] = objs[r], objs[l]
    if compare(objs[l], objs[end]) == 'greater':
        objs[l], objs[end] = objs[end], objs[l]
        return l
    else:
        return end

sorted_notebooks = quick_sort(notebooks, compare=compare_likes)
print(sorted_notebooks)
