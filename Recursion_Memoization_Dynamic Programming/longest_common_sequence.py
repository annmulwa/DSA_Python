def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0

    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1 + 1, idx2 + 1)
    else:
        option1 = lcs_recursive(seq1, seq2, idx1 + 1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)

# seq1 = 'abcde'
# seq2 = 'ace'
# seq1 = 'serendipitous'
# seq2 = 'precipitation'
seq1 = [1,2,3,4,5]
seq2 = [1,2,3,4,5,6]
# print(lcs_recursive(seq1, seq2))

# Memoization
def lcs_memo(seq1, seq2):
    memo = {}

    def recurse(idx1=0, idx2=0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1 + 1, idx2 + 1)
        else:
            memo[key] = max(recurse(idx1 + 1, idx2), recurse(idx1, idx2 + 1))
        return memo[key]
    return recurse(0, 0)

seq1 = 'serendipitous'
seq2 = 'precipitation'
print(lcs_memo(seq1, seq2))

# Dynamic Programming
# m, n = 5, 7
# result = [[0 for i in range(m)] for j in range(n)]
# print(result)
def lcs_dp(seq1, seq2):
    dp = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

    for i in range(len(seq1) - 1, -1, -1):
        for j in range(len(seq2) - 1, -1, -1):
            if seq1[i] == seq2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]

# seq1 = 'abcde'
# seq2 = 'ace'
seq1 = 'serendipitous'
seq2 = 'precipitation'
print(lcs_dp(seq1, seq2))

# Dynamic Programming(Top-Bottom)
def lcs_dp_tb(seq1, seq2):
    table = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])
    return table[-1][-1]

seq1 = 'serendipitous'
seq2 = 'precipitation'
print(lcs_dp_tb(seq1, seq2))
