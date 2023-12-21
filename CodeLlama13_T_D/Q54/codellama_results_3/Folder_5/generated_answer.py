
def all_right_truncatable_prime(numbers):
    right_truncatable_primes = []
    for number in numbers:
        if is_right_truncatable_prime(number):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)

def is_right_truncatable_prime(number):
    while number > 0:
        if not is_prime(number):
            return False
        number //= 10
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
