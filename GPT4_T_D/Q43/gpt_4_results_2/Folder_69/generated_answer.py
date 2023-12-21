
def find_primes_between_indices(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    
    primes = [n for n in numbers[497:931] if is_prime(n)]
    return sorted(primes, reverse=True)
