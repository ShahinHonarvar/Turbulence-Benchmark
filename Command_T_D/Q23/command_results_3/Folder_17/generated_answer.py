def find_divisors_in_range(n):
    if n < 10 or n > 69:
        return []
    a, b = 1, 1
    while b < n:
        a += 1
        b = a * 10
    return [x for x in range(10, n + 1, 10) if n % x == 0]
