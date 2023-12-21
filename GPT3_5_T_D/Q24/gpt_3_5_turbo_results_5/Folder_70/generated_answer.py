
def sum_of_divisors_in_range(n):
    if n < 586 or n > 840:
        return 0

    divisor_sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if 586 <= i <= 840:
                divisor_sum += i

    return divisor_sum
