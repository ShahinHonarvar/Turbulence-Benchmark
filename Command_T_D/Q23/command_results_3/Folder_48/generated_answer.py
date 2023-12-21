def find_divisors_in_range(n):
    d = [x for x in range(461, 827+1) if n % x == 0]
    if len(d) > 0:
        return d
    else:
        return []
