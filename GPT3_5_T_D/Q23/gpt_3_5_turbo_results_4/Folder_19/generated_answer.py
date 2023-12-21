
def find_divisors_in_range(n):
    divisor_list = []
    for i in range(1, 8):
        if n % i == 0:
            divisor_list.append(i)
    return divisor_list
