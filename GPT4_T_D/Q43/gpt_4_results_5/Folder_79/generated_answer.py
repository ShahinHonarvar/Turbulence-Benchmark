
def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False

def find_primes_between_indices(numbers):
    primes = [num for num in numbers[33:36] if is_prime(num)]
    primes.sort()
    return primes
