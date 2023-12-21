
def find_divisors_in_range(number):
    divisors = []
    for i in range(35, 99):
        if number % i == 0:
            divisors.append(i)
    return divisors
