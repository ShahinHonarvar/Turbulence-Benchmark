
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for num in numbers[19:72]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes)
