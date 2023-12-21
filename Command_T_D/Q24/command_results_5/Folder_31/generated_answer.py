def sum_of_divisors_in_range(N):
    if N < 35 or N > 55:
        return 0
    return N * (N + 1) * (2 * N + 1) // 6
