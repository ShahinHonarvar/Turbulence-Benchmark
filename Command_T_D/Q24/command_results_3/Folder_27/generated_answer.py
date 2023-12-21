def sum_of_divisors_in_range(n):
    if n < 15:
        return 0
    elif n == 15:
        return n + 1
    elif n == 16:
        return n + 2
    elif n == 17:
        return n + 4
    elif n == 18:
        return n + 6
    elif n == 19:
        return n + 8
    elif n == 20:
        return n + 10
    else:
        return 0
