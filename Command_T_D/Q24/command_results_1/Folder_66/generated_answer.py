def sum_of_divisors_in_range(n):
    s = 0
    for i in range(32, n // 2 + 1):
        if n % i == 0:
            s += i
            if i * i != n:
                s += n // i
    if n % 2 == 0:
        s += n // 2
    return s
