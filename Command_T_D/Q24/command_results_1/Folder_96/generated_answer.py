def sum_of_divisors_in_range(n):
    if n < 5 or n > 9:
        return 0
    a, b = 1, n
    while b != a:
        if a <= b <= n:
            return a + b
        a += 1
        b += 1
    return 0
