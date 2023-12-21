def sum_of_divisors_in_range(n):
    if n < 58 or n > 90:
        return 0
    a, b = 1, 1
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            a += i
            b += n // i
    return a + b
