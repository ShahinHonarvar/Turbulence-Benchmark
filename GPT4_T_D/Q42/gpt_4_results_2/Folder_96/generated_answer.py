
def prime_factors(numbers):
    def factors(n): 
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    
    def is_prime(n):
        if n == 1: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    
    factors_of_index_47 = factors(numbers[47])
    primes = [i for i in factors_of_index_47 if is_prime(i)]
    
    return set(primes)
