def solution(n):
    result = n // 10
    reminder = n % 10
    return result + reminder
#    num_str = str(n)
#    return (int(num_str[0]) + int(num_str[1]))

n = 29
print(solution(n))