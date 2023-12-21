import sys
def sum_of_divisors_in_range(n):
    #if no such divisors exist in the specified range, the function should return 0.
    if n < 32:
        return 0
    elif n > 90:
        return 0
    divisor_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisor_sum += i
            if n / i == i:
                divisor_sum += n / i
    return divisor_sum
