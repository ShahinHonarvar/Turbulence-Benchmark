
def all_left_truncatable_prime(numbers):
    primes = []
    for number in numbers:
        if is_prime(number) and not contains_zero(str(number)):
            primes.append(number)
    return sorted(primes, key=len)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s
