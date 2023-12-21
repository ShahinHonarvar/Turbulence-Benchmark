
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqr = int(n**0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    primes = [num for num in lst[261:460] if is_prime(num)]
    primes.sort()

    return primes
