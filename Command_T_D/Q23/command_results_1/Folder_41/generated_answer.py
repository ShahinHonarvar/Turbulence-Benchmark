def find_divisors_in_range(n):
    return [x for x in range(2, int(n ** .5) + 1) if n % x == 0]
