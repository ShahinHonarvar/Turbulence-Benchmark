
def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for i in range(1, n+1):
        if n % i == 0 and 6 <= i <= 7:
            divisor_sum += i
    return divisor_sum
