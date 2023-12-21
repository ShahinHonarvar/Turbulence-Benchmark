def all_right_truncatable_prime(n):
    for i in range(1, int(n[8] ** 0.5) + 1):
        if str(2 * i)[:-1] in str(2 * i):
            yield 2 * i
    for i in range(3, int(n[8] ** 0.5) + 1, 2):
        if str(2 * i)[:-1] in str(2 * i):
            yield 2 * i
