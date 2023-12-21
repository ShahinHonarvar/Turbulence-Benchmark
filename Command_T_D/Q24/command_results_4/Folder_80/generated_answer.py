def sum_of_divisors_in_range(n):
    if n < 70 or n > 93:
        return 0
    sum_of_divisors = 0
    for i in range(1, 1 + n // 2):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors
