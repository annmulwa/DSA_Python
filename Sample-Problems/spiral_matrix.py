def spiralMatrix(matrix):
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # get the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # get the right column
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # get the bottom row
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        # get the left col
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(spiralMatrix(matrix))