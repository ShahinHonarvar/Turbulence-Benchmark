def find_sum_of_multiples(n):
    result = 0
    for i in range(1, n + 1):
        result += i * n ** 2
    return result
