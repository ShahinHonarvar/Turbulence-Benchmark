
def find_primes_between_indices(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    primes = [i for i in numbers[0:2] if is_prime(i)]
    return sorted(primes)
