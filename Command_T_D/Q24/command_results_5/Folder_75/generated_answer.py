def sum_of_divisors_in_range(n):
    if n < 38 or n > 65:
        return 0
    return sum(i for i in range(1, int(n ** .5) + 1) if n % i == 0)
