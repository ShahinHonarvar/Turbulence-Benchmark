def sum_of_divisors_in_range(n):
    a, b = 35, 37
    s = 0
    while a <= b:
        if n % a == 0:
            s += a
        elif n % b == 0:
            s += b
        else:
            return s
        a += 1
        b -= 1
    return s
