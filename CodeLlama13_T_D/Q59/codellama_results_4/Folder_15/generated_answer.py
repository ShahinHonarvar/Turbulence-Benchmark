
def all_left_truncatable_prime(x):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    
    def left_truncatable_primes(x):
        primes = []
        for i in range(1, x):
            if is_prime(i):
                primes.append(i)
        
        truncatable_primes = []
        for prime in primes:
            if all(is_prime(int(str(prime)[1:])) for i in range(len(str(prime))-1)):
                truncatable_primes.append(prime)
        
        return truncatable_primes
    
    return sorted(left_truncatable_primes(x), reverse=True)
