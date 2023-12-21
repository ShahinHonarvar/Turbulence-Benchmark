def sum_of_divisors_in_range(n):
    s = 0
    for i in range(7, 9):
        if n % i == 0:
            s += i
            if n / i == i:
                s += n / i
    return s
