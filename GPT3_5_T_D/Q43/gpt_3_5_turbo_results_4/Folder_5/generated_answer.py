
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    index_range = range(27, 87)
    primes = [num for num in numbers[index_range] if is_prime(num)]
    return sorted(primes, reverse=True)
