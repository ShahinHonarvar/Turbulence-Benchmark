
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(prime):
    prime_str = str(prime)
    for i in range(1, len(prime_str)):
        if not is_prime(int(prime_str[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[975]
    truncatable_primes = []
    for i in range(x-1, 0, -1):
        if is_prime(i) and '0' not in str(i) and left_truncatable(i):
            truncatable_primes.append(i)
    return truncatable_primes
