
def find_divisors_in_range(num):
    divisors_list = [i for i in range(19, 70) if num % i == 0]
    return divisors_list
