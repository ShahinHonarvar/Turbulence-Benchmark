
def all_right_truncatable_prime(numbers):
    primes = []
    for number in numbers:
        if is_right_truncatable_prime(number):
            primes.append(number)
    return sorted(primes)

def is_right_truncatable_prime(number):
    if number < 10:
        return False
    for i in range(1, int(str(number)[::-1]) + 1):
        if not is_prime(number - i):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
