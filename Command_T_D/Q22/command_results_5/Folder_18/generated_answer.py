def find_sum_of_multiples(n):
    if n < 2:
        return 0
    return n * (n + 1) * (2 * n + 1) / 6
