def sum_of_divisors_in_range(x):
    s = 0
    for i in range(3, 9):
        if x % i == 0:
            s += i
            if x // i == i:
                s += x / i
    return s
