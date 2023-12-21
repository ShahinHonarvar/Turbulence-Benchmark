def sum_of_divisors_in_range(n):
    x = n // 2
    y = n // 3
    z = n // 5
    if x == 1 or x == 2 or x == 3 or x == 5:
        return x
    if y == 1 or y == 2 or y == 3 or y == 5:
        return y
    if z == 1 or z == 2 or z == 3 or z == 5:
        return z
    return 0
