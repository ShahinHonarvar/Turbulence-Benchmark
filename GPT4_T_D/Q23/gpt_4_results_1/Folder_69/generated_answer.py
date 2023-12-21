
def find_divisors_in_range(number):
    divisors = []
    for i in range(658, 869):
        if number % i == 0:
            divisors.append(i)
    return divisors
