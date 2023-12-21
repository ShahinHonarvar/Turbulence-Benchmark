def find_divisors_in_range(n):
    if n < 121 or n > 348:
        return []
    i = 2
    while i * i <= n:
        if n % i == 0:
            j = i
            while n % j == 0:
                n //= j
                j *= 2
            j += 1
            while n % j == 0:
                n //= j
                j *= 2
            yield i * i
            i *= 3
    if n > 1:
        yield n
