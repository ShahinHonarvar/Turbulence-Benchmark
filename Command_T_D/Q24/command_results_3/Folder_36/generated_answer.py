def sum_of_divisors_in_range(x):
    if x < 113:
        return 0
    x += 1
    s = 1
    for i in range(1, x):
        if x % i == 0:
            s += i
    return s
