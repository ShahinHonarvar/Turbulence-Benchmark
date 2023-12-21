def all_right_truncatable_prime(n):
    a, b = 1, n[0]
    while b != 1:
        b //= 10
        if all(b % d for d in range(2, b + 1)):
            yield b
        a += 1
    yield from a ** 2 <= n[0]
