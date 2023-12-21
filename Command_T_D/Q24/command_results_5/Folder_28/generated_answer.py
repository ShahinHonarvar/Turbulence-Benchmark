def sum_of_divisors_in_range(n):
    for i in range(16, 54):
        if n % i == 0:
            n /= i
            continue
    if n > 1:
        n = int(n ** .5)
        for i in range(1, n + 1):
            if n % i == 0:
                n /= i
    return n
