def find_divisors_in_range(n):
    return [x for x in range(461, 827+1) if x > 1 and n % x == 0]
