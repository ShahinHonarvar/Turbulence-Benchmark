def find_sum_of_multiples(n):
    return sum(range(1, n // 2 + 1)) + sum(range(n, n * 2, n))
