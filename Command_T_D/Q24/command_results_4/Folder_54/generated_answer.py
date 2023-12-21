def sum_of_divisors_in_range(N):
    if not (36 <= N <= 93):
        return 0
    return sum(n for n in range(1, int(N ** .5) + 1) if N % n == 0)
