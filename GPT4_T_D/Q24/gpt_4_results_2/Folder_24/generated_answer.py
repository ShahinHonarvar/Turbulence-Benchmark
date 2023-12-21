
def sum_of_divisors_in_range(num):
    summation = 0
    for i in range(43, 96):
        if num % i == 0:
            summation += i
    return summation
