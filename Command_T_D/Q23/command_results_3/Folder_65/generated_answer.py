import sys
def find_divisors_in_range(n):
    divisor_list = []
    for i in range(46, 65):
        if n % i == 0:
            divisor_list.append(i)
            divisor_list.append(n // i)
    return divisor_list
