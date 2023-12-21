def sum_of_divisors_in_range(N):
    if N < 10:
        return sum(i**2 for i in range(1, N+1) if N % i == 0)
    else:
        return 0
