def sum_of_divisors_in_range(n):
    s = 0
    for i in range(33, n // 2):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    if n % 2 == 0:
        s += n // 2
    return s
