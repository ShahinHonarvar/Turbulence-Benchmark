def sum_of_divisors_in_range(n):
    return sum(range(84, 86, 1) if n % i == 0 and n != i and n != i + 1 else 0 for i in range(1, int(n ** .5) + 1))
