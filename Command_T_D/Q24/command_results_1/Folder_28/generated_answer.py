def sum_of_divisors_in_range(n):
    if n < 16:
        return 0
    elif n > 53:
        return 0
    else:
        divisor_sum = 0
        for i in range(1, int(n ** .5) + 1):
            if n % i == 0:
                divisor_sum += i + n // i
        return divisor_sum
