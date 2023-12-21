
def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for i in range(46, 66):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum
