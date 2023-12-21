
def all_left_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)

def is_left_truncatable_prime(num):
    if num < 2 or any(num % i == 0 for i in range(2, int(num ** 0.5) + 1)):
        return False
    for i in range(2, len(str(num))):
        if not is_prime(int(str(num)[i:])):
            return False
    return True

def is_prime(num):
    if num < 2 or any(num % i == 0 for i in range(2, int(num ** 0.5) + 1)):
        return False
    return True
