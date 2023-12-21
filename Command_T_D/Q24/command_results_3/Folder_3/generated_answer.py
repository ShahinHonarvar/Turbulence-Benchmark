def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i >= 43 and i <= 46:
                divisor_sum += i
            if i * i == n:
                divisor_sum += n // i
    return divisor_sum
