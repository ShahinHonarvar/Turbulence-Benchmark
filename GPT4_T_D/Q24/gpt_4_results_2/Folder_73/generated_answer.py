
def sum_of_divisors_in_range(n):
    if n < 46:
        return 0
    else:
        divisor_sum = 0
        for i in range(46, 90):
            if n % i == 0:
                divisor_sum += i
        return divisor_sum
