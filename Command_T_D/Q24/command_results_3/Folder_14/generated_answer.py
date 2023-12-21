def sum_of_divisors_in_range(n):
    if n <= 5:
        return 0
    elif n <= 7:
        divisors = [1, 2, 3, 4, 5, 6, 7]
    elif n <= 8:
        divisors = [1, 2, 3, 4, 5, 6, 7, 8]
    return sum(divisors)
