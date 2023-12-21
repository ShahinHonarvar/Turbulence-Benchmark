def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for i in range(5, 7):
        if n % i == 0:
            divisor_sum += i
            if i * i != n:
                divisor_sum += n // i
    return divisor_sum
