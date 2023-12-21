def sum_of_divisors_in_range(N):
    return sum(range(1, min(N, 41) + 1, 2) + range(min(N, 41), max(N, 55) + 1))
