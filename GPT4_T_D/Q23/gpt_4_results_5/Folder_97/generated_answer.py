
def find_divisors_in_range(number):
    divisor_list = []
    for i in range(615, 793):
        if number % i == 0:
            divisor_list.append(i)
    return divisor_list
