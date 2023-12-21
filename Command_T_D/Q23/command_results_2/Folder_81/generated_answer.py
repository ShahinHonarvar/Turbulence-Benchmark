def find_divisors_in_range(n):
    if n == 1:
        return []
    elif n == 2:
        return [3, 4]
    else:
        return [x for x in range(3, n // 2 + 1, 2) if n % x == 0]
