def sum_of_divisors_in_range(n):
    # If no such divisors exist in the specified range, the function should return 0.
    # n = 387
    # n = 516
    # print(sum_of_divisors_in_range(n))
    if n <= 387:
        # return n / 2 + (n + 1) / 2
        return n / 2 + (n + 1) / 2
    elif n <= 516:
        # return n / 2 + (n + 1) / 2
        return n / 2 + (n + 1) / 2
    else:
        # return 0
        return 0
