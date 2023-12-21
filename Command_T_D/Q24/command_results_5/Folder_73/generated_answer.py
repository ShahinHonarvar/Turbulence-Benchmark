def sum_of_divisors_in_range(N):
    result = 0
    for i in range(46, 89 + 1):
        if N % i == 0:
            result += i + N / i
    return result
