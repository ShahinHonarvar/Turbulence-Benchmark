def find_divisors_in_range(n):
    return [x for x in range(3, n + 1) if all(n % i == 0 for i in range(3, int(n ** .5) + 1))]
