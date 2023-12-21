
def all_left_right_truncatable_prime(numbers):
    primes = []
    for n in numbers:
        if is_prime(n) and contains_no_zeroes(str(n)):
            primes.append(n)
    return sorted(primes, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_no_zeroes(s):
    return '0' not in s
