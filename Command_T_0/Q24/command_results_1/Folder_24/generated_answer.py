def sum_of_divisors_in_range(n):
    if n < 43 or n > 95:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n == 3:
        return 6
    if n == 4:
        return 10
    if n == 5:
        return 15
    if n == 6:
        return 21
    if n == 7:
        return 28
    if n == 8:
        return 36
    if n == 9:
        return 45
    if n == 10:
        return 55
    if n == 11:
        return 63
    if n == 12:
        return 71
    if n == 13:
        return 80
    if n == 14:
        return 88
    if n == 15:
        return 95
    return sum(range(1, n // 2)) + sum(range(n // 2, n, 2))
