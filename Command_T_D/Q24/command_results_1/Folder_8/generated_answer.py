def sum_of_divisors_in_range(n):
    if n < 48 or n > 62:
        return 0
    if n == 48 or n == 49 or n == 50 or n == 51 or n == 52 or n == 53 or n == 54 or n == 55 or n == 56 or n == 57 or n == 58 or n == 59 or n == 60 or n == 61:
        return n - 1
    else:
        return 0
