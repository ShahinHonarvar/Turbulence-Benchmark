def sum_of_divisors_in_range(n):
    s = 0
    for i in range(2, n + 1):
        if n % i == 0:
            s += i
    if n == 1:
        s += 1
    return s
