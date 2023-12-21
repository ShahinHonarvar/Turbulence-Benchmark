
def all_right_truncatable_prime(numbers):
    prime_numbers = []
    for number in numbers:
        if is_right_truncatable_prime(number):
            prime_numbers.append(number)
    return sorted(prime_numbers)

def is_right_truncatable_prime(number):
    if number < 10:
        return False
    for i in range(1, len(str(number))):
        if not is_prime(number % (10 ** i)):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
