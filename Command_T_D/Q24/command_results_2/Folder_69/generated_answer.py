def sum_of_divisors_in_range(n):
    if n <= 657:
        return 0
    if n <= 867:
        return sum(i for i in range(2, n//2 + 1) if n % i == 0)
    return sum(i for i in range(2, n//2 + 1) if n % i == 0) + sum(j for j in range(n//2, n//2 + n//2 + 1) if n % j == 0)
