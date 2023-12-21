def sum_of_divisors_in_range(n):
    s = sum(i * i for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return s if s <= 681 else 0
