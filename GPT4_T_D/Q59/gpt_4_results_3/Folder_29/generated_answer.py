
def all_left_truncatable_prime(tup):
    import sympy
    
    def is_left_truncatable_prime(n):
        if '0' in str(n): 
            return False
        else: 
            return all(sympy.isprime(int(str(n)[i:])) for i in range(len(str(n)))) 

    x = tup[55]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)
