def sum_of_divisors_in_range(n):
    a = 372
    b = 494
    s = 0
    while a <= n:
        if n % a == 0:
            s += a
            n /= a
        elif n % b == 0:
            s += b
            n /= b
        else:
            a += 1
            b += 1
    return s
