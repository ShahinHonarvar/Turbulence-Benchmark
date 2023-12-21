
def find_divisors_in_range(num):
    divisors_in_range = []
    for i in range(4, 10):
        if num % i == 0:
            divisors_in_range.append(i)
    return divisors_in_range
