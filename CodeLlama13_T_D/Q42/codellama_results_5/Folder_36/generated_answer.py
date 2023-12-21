
def prime_factors(numbers):
    return set([number for number in numbers[990] if is_prime_factor(number)])

def is_prime_factor(number):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
