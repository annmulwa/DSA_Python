# using recursion
# Time Complexity: O(3^(n + m))
# Space Complexity: O(n + m)
def lcs(s, t, i=0, j=0, count=0):
    if i == len(s) or j == len(t):
        return count
    elif s[i] == t[j]:
        return lcs(s, t, i + 1, j + 1, count + 1)
    else:
        option1 = lcs(s, t, i + 1, j, 0)
        option2 = lcs(s, t, i, j + 1, 0)

        return max(count, option1, option2)

s = "zxabcdezy"
t = "yzabcdezx"
print(lcs(s, t))

# using memoization
# Time Complexity: O(n × m × min(n, m))
# Space Complexity: O(n × m × min(n, m))
def lcs_memo(s, t):
    memo = {}

    def recurse(i=0, j=0, count=0):
        key = (i, j, count)
        if key in memo:
            return memo[key]
        elif i == len(s) or j == len(t):
            return count
        elif s[i] == t[j]:
            return recurse(i + 1, j + 1, count + 1)
        else:
            option1 = recurse(i + 1, j, 0)
            option2 = recurse(i, j + 1, 0)
            memo[key] = max(count, option1, option2)
        return memo[key]
    return recurse(0, 0, 0)

s = "zxabcdezy"
t = "yzabcdezx"
print(lcs_memo(s, t))

# using dp(bottom-up)
# Time Complexity: O(n × m)
# Space Complexity: O(n × m)
def lcs_dp(s, t):
    dp = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    max_length = 0

    for i in range(len(s) - 1, -1, -1):
        for j in range(len(t) - 1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
    return max_length

# s = "zxabcdezy"
# t = "yzabcdezx"
s = "abcdaf"
t = "zbcdf"
print(lcs_dp(s, t))