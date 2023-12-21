def find_divisors_in_range(n):
    if n < 472 or n > 827:
        return []
    a = n**0.5
    return [d for d in range(1, int(a) + 1) if n % d == 0]
