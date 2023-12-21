
def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for number in numbers:
        if is_left_and_right_truncatable_prime(number):
            left_right_truncatable_primes.append(number)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_left_and_right_truncatable_prime(number):
    if number % 10 == 0:
        return False
    for i in range(1, len(str(number)) // 2 + 1):
        prime = number % (10 ** i)
        if not is_prime(prime):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
