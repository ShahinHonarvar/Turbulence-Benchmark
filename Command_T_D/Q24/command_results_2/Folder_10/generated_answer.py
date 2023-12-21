def sum_of_divisors_in_range(n):
    if n <= 60 or n >= 86:
        return 0
    a, b = 1, n // 2
    while a <= n // 2:
        if n % a == 0:
            if a <= 60:
                yield a
            elif b >= 86:
                yield b
            else:
                a += 1
                b -= 1
    if n % 2 == 0:
        yield n // 2
    if n % 3 == 0:
        yield n // 3
