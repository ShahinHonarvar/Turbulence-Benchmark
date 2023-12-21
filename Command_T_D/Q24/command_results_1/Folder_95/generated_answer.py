def sum_of_divisors_in_range(n):
    if n <= 35 or n >= 98:
        return 0
    sum_of_divisors_in_range = 0
    for x in range(1, 1 + int(n ** .5)):
        if n % x == 0:
            sum_of_divisors_in_range += x + n / x
    return sum_of_divisors_in_range
