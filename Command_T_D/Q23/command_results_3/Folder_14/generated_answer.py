def find_divisors_in_range(n):
    if n < 6:
        return []
    elif n < 8:
        return [x for x in range(6, n//2 + 1) if n % x == 0]
    else:
        return []
