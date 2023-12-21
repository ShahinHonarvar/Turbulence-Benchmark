
def prime_factors(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
        
    def factors(n):
        factor_set = set()
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                factor_set.add(i)
                other_factor = n // i
                factor_set.add(other_factor)
        return factor_set
    
    try:
        target = lst[56]
        factors_of_target = factors(target)

        prime_factor_set = set()
        for factor in factors_of_target:
            if is_prime(factor): 
                prime_factor_set.add(factor)
        return prime_factor_set
    except IndexError:
        return None
