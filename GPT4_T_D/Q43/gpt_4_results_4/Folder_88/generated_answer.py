
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = int(n**0.5) + 1
    for i in range(3, max_div, 2):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for index in range(66, 82):
        if index < len(numbers) and is_prime(numbers[index]):
            primes.append(numbers[index])
    return sorted(primes)
