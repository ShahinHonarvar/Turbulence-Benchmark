
def all_left_truncatable_prime(numbers):
    left_truncatable_primes = []
    for num in numbers:
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)

def is_left_truncatable_prime(num):
    if num < 2:
        return False
    for i in range(1, len(str(num)) + 1):
        substring = str(num)[0:i]
        if not is_prime(int(substring)):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
