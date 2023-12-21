def find_divisors_in_range(n):
    if n < 70 or n > 72:
        return []
    d = [x for x in range(1, 1 + int(n ** .5) + 1) if n % x == 0]
    return d if 70 <= min(d) <= 72 else []
