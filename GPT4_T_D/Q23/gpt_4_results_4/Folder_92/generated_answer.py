
def find_divisors_in_range(num):
    divisor_list = []
    for i in range(8, 10):
        if num % i == 0:
            divisor_list.append(i)
    return divisor_list
