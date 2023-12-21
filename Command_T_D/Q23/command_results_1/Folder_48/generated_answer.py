def find_divisors_in_range(n):
    if n < 461:
        return []
    elif n > 827:
        return []
    else:
        return [k for k in range(461, 827) if n % k == 0]
