import sys
def find_divisors_in_range(n):
    divisor_list = []
    for i in range(38, 65):
        if n%i == 0:
            divisor_list.append(i)
            if i*i != n:
                divisor_list.append(n//i)
    return divisor_list
