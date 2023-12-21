
def find_divisors_in_range(number):
    divisor_list = [i for i in range(10, 56) if number % i == 0]
    return divisor_list
