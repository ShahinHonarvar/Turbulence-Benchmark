
def find_primes_between_indices(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = [x for x in numbers[46:62] if is_prime(x)]
    primes.sort()
    return primes
