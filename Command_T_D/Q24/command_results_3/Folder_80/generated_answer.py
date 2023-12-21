def sum_of_divisors_in_range(n):
    70 <= n <= 93
    divisor_sum = 1
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i * i != n:
                divisor_sum += n // i
    if n % 2 == 0:
        divisor_sum += 2
    if n % 3 == 0:
        divisor_sum += 3
    return divisor_sum
