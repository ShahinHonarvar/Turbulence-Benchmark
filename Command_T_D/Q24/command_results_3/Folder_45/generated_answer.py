def sum_of_divisors_in_range(n):
    if n < 4 or n > 8:
        return 0
    s = 1
    i = 1
    while i * i <= n:
        if n % i == 0:
            j = i
            while n % j == 0:
                n //= j
                s += n
                j += 1
        i += 1
    if n > 1:
        s += n
    return s
