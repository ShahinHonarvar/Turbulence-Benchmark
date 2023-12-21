def sum_of_divisors_in_range(n):
    if n < 42 or n > 55:
        return 0
    a, b = 1, n
    while a <= b:
        if n % a == 0:
            a += 1
        elif n % b == 0:
            b -= 1
        else:
            a += 1
    return a - 1
