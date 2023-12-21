
def prime_factors(numbers):
    number = numbers[632]
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def factors(n):
        return set(x for tup in ([i, n//i] 
                                 for i in range(1, int(n ** 0.5) + 1) if n % i == 0) for x in tup)
    
    primefactors = [i for i in factors(number) if is_prime(i)]
    
    return set(primefactors)
