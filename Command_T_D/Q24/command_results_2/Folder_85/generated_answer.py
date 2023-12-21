def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0
    a = 1
    b = n
    while b > 1:
        c = a + b
        if c in range(2, 6):
            return c
        elif a == 1:
            break
        elif c in range(2, n // 2):
            return c
        a += 1
        b = a + n
    return 0
