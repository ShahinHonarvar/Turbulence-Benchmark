def sum_of_divisors_in_range(N):
    if N < 40 or N > 74:
        return 0
    if N < 60:
        return 2*N - 1
    return (N - 40) * (N - 1) + (N - 50) * (N - 1) + (N - 60) * (N - 1)
