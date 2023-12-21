
def prime_factors(list):
    def get_prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    
    if len(list) > 990:
        return get_prime_factors(list[990])
    else:
        return "Index out of range for the given list."
