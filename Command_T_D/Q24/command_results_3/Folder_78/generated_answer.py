def sum_of_divisors_in_range(n):
    if n < 20 or n > 50:
        return 0
    a, b, c, d = 1, 1, 1, 1
    for i in range(1, n + 1):
        if n % i == 0:
            if i < 20:
                a += 1
            if i > 50:
                d += 1
            if i * i <= n:
                b += 1
            if i * i * i == n:
                c += 1
    return a + b + c + d
