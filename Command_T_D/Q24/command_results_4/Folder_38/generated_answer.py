def sum_of_divisors_in_range(n):
    if n <= 16 or n >= 68:
        return 0
    a = n**0.5
    for b in range(16, a + 1):
        if b * b == a:
            c = n / b
            if c <= a:
                yield b + 1
                yield c + 1
    yield n + 1
