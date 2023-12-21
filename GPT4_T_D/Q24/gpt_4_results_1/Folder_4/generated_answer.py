
def sum_of_divisors_in_range(n):
    sum_div = 0
    for i in range(48, 61):
        if n % i == 0:
            sum_div += i
    return sum_div
