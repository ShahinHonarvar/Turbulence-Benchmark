
def prime_factors(lst):
    def prime(n):
        if n < 2: return []
        factors = []
        for i in range(2, n+1):
            while n % i == 0 :
                factors.append(i)
                n /= i
        return factors
    
    return set(prime(lst[21]))
