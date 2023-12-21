def sum_of_divisors_in_range(n):
    result = 0
    for i in range(1, n + 1):
        for j in range(1, int(n ** .5) + 1):
            if i * j > n:
                break
            if i in range(48, 62) and j in range(48, 62):
                result += i * j
    return result
