
def find_divisors_in_range(number):
    divisors = []
    for i in range(1, 3):
        if number % i == 0:
            divisors.append(i)
    return divisors
