def find_sum_of_multiples(n):
    result = 0
    for i in range(1, n + 1):
        for j in range(i * 2, n + 1, i):
            result += j
    return result
