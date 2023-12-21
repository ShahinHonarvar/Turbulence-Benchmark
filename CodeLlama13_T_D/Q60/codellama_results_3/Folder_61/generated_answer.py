
def all_left_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            prime_numbers.append(i)
    left_and_right_truncatable_primes = []
    for i in prime_numbers:
        if is_left_and_right_truncatable_prime(i):
            left_and_right_truncatable_primes.append(i)
    return sorted(left_and_right_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s

def is_left_and_right_truncatable_prime(n):
    while len(str(n)) > 1:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True
