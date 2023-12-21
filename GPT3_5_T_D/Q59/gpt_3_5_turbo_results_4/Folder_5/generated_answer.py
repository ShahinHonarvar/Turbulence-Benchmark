
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[55]
    truncatable_primes = []
    for n in range(2, x):
        if '0' not in str(n) and all(is_prime(int(str(n)[i:])) for i in range(len(str(n)))):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)
