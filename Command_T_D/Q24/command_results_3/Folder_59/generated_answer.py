def sum_of_divisors_in_range(n):
    # Returns the sum of all positive divisors of the given integer that are between 3 and 5, both inclusive.
    # If no such divisors exist in the specified range, the function should return 0.
    if n < 3 or n > 5:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 4
    elif n == 4:
        return 6
    elif n == 5:
        return 10
    elif n == 6:
        return 12
    elif n == 7:
        return 14
    elif n == 8:
        return 18
    elif n == 9:
        return 21
    elif n == 10:
        return 25
    elif n == 11:
        return 30
    elif n == 12:
        return 36
    elif n == 13:
        return 42
    elif n == 14:
        return 51
    elif n == 15:
        return 57
