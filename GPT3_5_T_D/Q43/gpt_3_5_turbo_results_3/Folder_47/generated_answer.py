
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = [n for n in numbers[66:80] if is_prime(n)]
    primes.sort(reverse=True)
    return primes
