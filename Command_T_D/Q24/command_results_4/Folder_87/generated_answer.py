def sum_of_divisors_in_range(n):
    s = sum(i for i in range(1, n + 1) if all(j % i == 0 for j in range(1, min(n, i**2) + 1)))
    return s if s > 50 and s <= 81 else 0
