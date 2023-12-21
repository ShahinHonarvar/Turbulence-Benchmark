
def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and not contains_zero(str(num)):
            primes.append(num)
    return primes

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s
