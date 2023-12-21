
def all_left_truncatable_prime(numbers):
    left_truncatable_primes = []
    for number in numbers:
        if is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    return sorted(left_truncatable_primes)

def is_left_truncatable_prime(number):
    if number < 2:
        return False
    for i in range(1, len(str(number)) + 1):
        if not is_prime(int(str(number)[i:])):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
