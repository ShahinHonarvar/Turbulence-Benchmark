def sum_of_divisors_in_range(n):
    return sum(range(n**0.5, 86, n) if n**0.5 % 1 == 0 else range(57, n//2))
