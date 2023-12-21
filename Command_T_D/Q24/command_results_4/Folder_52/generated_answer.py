def sum_of_divisors_in_range(n):
    if n == 1:
        return 0
    for i in range(2, 1 + int(n ** .5)):
        if n % i == 0:
            if 70 <= i <= 72:
                return i + i + 1
            else:
                return 0
    return 0
