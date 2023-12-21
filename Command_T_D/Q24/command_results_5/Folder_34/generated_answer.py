def sum_of_divisors_in_range(n):
    if n < 4 or n > 5:
        return 0
    i = 2
    while i <= n:
        if n % i == 0:
            j = i
            while j * i <= n:
                j *= i
                n -= j
                i += 1
            i += 1
    return n // 2
