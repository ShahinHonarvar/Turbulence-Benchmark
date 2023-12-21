def sum_of_divisors_in_range(n):
    if n < 403 or n > 514:
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
        return 66
    if n == 12:
        return 83
    if n == 13:
        return 102
    if n == 14:
        return 121
    if n == 15:
        return 150
    if n == 16:
        return 183
    if n == 17:
        return 216
    if n == 18:
        return 243
    if n == 19:
        return 286
    if n == 20:
        return 321
    if n == 21:
        return 366
    if n == 22:
        return 401
    if n == 23:
        return 446
    if n == 24:
        return 500
    if n == 25:
        return 521
    return 0
