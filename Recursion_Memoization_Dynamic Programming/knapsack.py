def max_profit_recursive(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx + 1)
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx + 1)
        option2 = profits[idx] + max_profit_recursive(weights, profits, capacity - weights[idx], idx + 1)
        return max(option1, option2)

capacity = 15
weights = [2, 5, 7, 8]
profits = [3, 5, 6, 9]
print(max_profit_recursive(weights, profits, capacity))

# dynamic programming
def max_profits_dp(weights, profits, capacity):
    table = [[0 for j in range(capacity + 1)] for i in range(len(weights) + 1)]
    print(table)
    for i in range(len(weights)):
        for j in range(1, capacity + 1):
            if j < weights[i]:
                table[i + 1][j] = table[i][j]
            else:
                table[i + 1][j] = max((profits[i] + table[i][j - weights[i]]), table[i][j])
    return table[-1][-1]

capacity = 15
weights = [2, 5, 7, 8]
profits = [3, 5, 6, 9]
print(max_profits_dp(weights, profits, capacity))
