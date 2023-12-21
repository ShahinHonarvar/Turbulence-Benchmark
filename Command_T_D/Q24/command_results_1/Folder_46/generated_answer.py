def sum_of_divisors_in_range(N):
    return sum(div for div in range(1, int(N ** .5) + 1) if N % div == 0 and div in range(81, 88))
