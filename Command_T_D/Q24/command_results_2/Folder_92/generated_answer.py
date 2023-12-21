def sum_of_divisors_in_range(n):
    s = 0
    if n >= 8:
        for i in range(n, 9, 1):
            if n % i == 0:
                s += i
        return s
    else:
        return 0
