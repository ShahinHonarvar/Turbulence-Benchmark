
def all_right_truncatable_prime(numbers):
    right_truncatable_primes = []
    for number in numbers:
        if is_right_truncatable_prime(number):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)

def is_right_truncatable_prime(number):
    if number % 2 == 0 or number < 3:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
