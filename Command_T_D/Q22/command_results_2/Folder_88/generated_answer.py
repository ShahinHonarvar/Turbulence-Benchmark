def find_sum_of_multiples(n):
    result = 0
    for i in range(1, n + 1):
        for j in range(1, 24):
            if i % j == 0:
                result += i
    return result
