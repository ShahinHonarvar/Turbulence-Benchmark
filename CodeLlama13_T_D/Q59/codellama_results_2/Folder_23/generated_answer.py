
def all_left_truncatable_prime(numbers):
    left_truncatable_primes = []
    for number in numbers:
        if is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    return sorted(left_truncatable_primes, reverse=True)

def is_left_truncatable_prime(number):
    if number < 2:
        return False
    for i in range(1, len(str(number))):
        truncated_number = int(str(number)[i:])
        if truncated_number % 2 == 0 or truncated_number % 5 == 0:
            return False
    return True
