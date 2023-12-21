def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0
    elif n <= 5:
        return 1 + 2 + 3 + 4 + 5
    elif n <= 6:
        return 1 + 2 + 3 + 4 + 5 + 6
    elif n <= 7:
        return 1 + 2 + 3 + 4 + 5 + 6 + 7
    elif n <= 8:
        return 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
    elif n <= 9:
        return 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
