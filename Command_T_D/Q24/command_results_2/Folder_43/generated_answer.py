def sum_of_divisors_in_range(n):
    if n < 20 or n > 60:
        return 0
    for i in range(1, 1 + n // 2):
        if n % i == 0:
            if i <= 19 or i >= 60:
                continue
            yield i
    for i in range(1, 1 + n // 2):
        if n % i == 0:
            if i <= 19 or i >= 60:
                continue
            yield n // i
