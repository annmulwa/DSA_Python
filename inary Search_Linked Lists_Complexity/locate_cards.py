#BRUTE FORCE SOLUTION - LINEAR SEARCH
# def locate_card(cards, query):
#     #create a variable position and initialize with 0
#     position = 0

#     print('cards:', cards)
#     print('query:', query)

#     #initialize the loop
#     while position < len(cards):

#         print('position:', position)

#         #check if the card in that position has the same number as the query
#         if (cards[position] == query):
#             return position

#         #if not increment the position
#         position += 1

#     #if you reach the end of the cards without finding the number in the query return -1
#     return -1

# OPTIMAL SOLUTION - BINARY SEARCH
# def locate_card(cards, query):
#     low, high = 0, len(cards) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         mid_number = cards[mid]

#         if mid_number == query:
#             return mid
#         elif mid_number > query:
#             low = mid + 1
#         elif mid_number < query:
#             high = mid - 1
#     return -1

# INCASE OF REPEATING CORRECT QUERIES
def test_location(cards, query, mid):
    mid_number = cards[mid]

    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        return 'found'
    elif mid_number > query:
        return 'right'
    else:
        return 'left'

def locate_card(cards, query):
    low, high = 0, len(cards) - 1

    while low <= high:
        mid = (low + high) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1
    return -1

result = locate_card([13,12,10,4,4,4,3,2,1], 4)
print(result)
