
def find_divisors_in_range(number):
    divisors = []
    for i in range(224, 585):
        if number % i == 0:
            divisors.append(i)
    return divisors
