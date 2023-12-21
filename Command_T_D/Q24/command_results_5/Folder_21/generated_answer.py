def sum_of_divisors_in_range(N):
    return sum(div for div in range(120, 349) if all(N % i == 0 for i in range(1, int(N ** .5) + 1)))
