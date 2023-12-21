
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def find_primes_between_indices(numbers):
    slice = numbers[87:90]
    primes = [num for num in slice if is_prime(num)]
    primes.sort()
    return primes
