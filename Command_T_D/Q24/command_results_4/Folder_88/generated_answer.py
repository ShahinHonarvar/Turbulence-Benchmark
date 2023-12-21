def sum_of_divisors_in_range(n):
    if n < 6 or n > 7:
        return 0
    sum_of_divisors = 1
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            sum_of_divisors += i + n / i
    if n % 2 == 0 and n % 3 == 0:
        sum_of_divisors += n / 2 + n / 3
    return sum_of_divisors
