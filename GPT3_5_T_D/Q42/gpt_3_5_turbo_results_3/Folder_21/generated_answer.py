
def prime_factors(integer_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    integer = integer_list[410]
    factors = set()
    for i in range(2, int(integer**0.5) + 1):
        if integer % i == 0:
            if is_prime(i):
                factors.add(i)
            if is_prime(integer // i):
                factors.add(integer // i)
    
    return factors
