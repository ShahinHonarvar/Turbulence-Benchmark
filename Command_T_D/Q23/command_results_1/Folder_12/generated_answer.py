def find_divisors_in_range(n):
    if n < 13 or n > 62:
        return []
    a, b = 13, n - 1
    i = 1
    while a <= b:
        if n % a == 0:
            yield a
            b = a - 1
        a += 1
        if b == 0:
            yield n
            break
        if n % b == 0:
            yield b
            a = b + 1
    return
