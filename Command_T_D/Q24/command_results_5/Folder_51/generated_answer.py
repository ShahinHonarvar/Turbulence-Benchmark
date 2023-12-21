def sum_of_divisors_in_range(n):
    if n < 2 or n > 7:
        return 0
    a, b, c, d, e, f = 2, 3, 4, 6, 1, 2
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            a += i
            b += i * n // i
            c += i * n // i
            d += i * n // i
            e += i * n // i
            f += i * n // i
    return a + b + c + d + e + f
