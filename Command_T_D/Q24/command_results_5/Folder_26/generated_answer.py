def sum_of_divisors_in_range(n):
    a = 83
    b = 95
    s = 0
    for i in range(a, b + 1):
        if n % i == 0:
            s += i
            if n / i != i:
                s += n / i
    return s
