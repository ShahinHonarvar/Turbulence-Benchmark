
def all_left_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_left_truncatable_prime(num):
    if not isinstance(num, int) or num < 2:
        return False
    for i in range(1, len(str(num))):
        if str(num)[i] == '0':
            return False
        if not is_prime(int(str(num)[:i])):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
