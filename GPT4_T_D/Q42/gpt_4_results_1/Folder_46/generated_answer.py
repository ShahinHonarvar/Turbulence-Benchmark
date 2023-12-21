
def prime_factors(numbers):
    def primes(n):
        i = 2 
        prime_factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                prime_factors.add(i)
        if n > 1:
            prime_factors.add(n)
        return prime_factors

    return primes(numbers[453])
