
def all_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
    sorted_primes = sorted(prime_numbers, reverse=True)
    right_truncatable_primes = []
    for p in sorted_primes:
        p_str = str(p)
        if is_right_truncatable_prime(p_str):
            right_truncatable_primes.append(p)
    return right_truncatable_primes

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(p_str):
    for i in range(len(p_str)):
        if not is_prime(int(p_str[:-i])):
            return False
    return True
