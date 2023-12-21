def find_divisors_in_range(n):
    if n < 27:
        return []
    elif n < 44:
        return [x for x in range(1, n + 1) if all(x % y == 0 for y in range(1, int(x ** .5) + 1))]
    else:
        return []
