
import itertools

def is_prime(n):
    if n == 1 or (n != 2 and n % 2 == 0):
        return False
    for current in range(3, int(n ** 0.5) + 1, 2):
        if n % current == 0: 
            return False
    return True

def primes(n):
    digits = "123456789"
    primes = ["2","3","5","7"]
    for length in range(2, n):
        for prime in primes:
            if len(prime) == length - 1:
                for digit in digits:
                    num = prime + digit
                    if is_prime(int(num)):
                        primes.append(num)
    return primes
    
def all_left_truncatable_prime(t):
    max_prime_length = len(str(t[39])) + 1
    all_primes = primes(max_prime_length)

    return sorted([int(x) for x in all_primes if all(is_prime(int(x[i:])) for i in range(len(x))) and int(x) < t[39]], reverse=True)
