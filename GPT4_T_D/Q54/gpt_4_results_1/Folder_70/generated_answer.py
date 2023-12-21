
def all_right_truncatable_prime(tup):
    import sympy
    x = tup[433]
    
    def check_right_truncatable_prime(n):
        if n == 0:
            return True
        elif sympy.isprime(n):
            return check_right_truncatable_prime(n//10)
        else:
            return False
    
    result = []
    for i in range(x):
        if check_right_truncatable_prime(i):
            result.append(i)
            
    result.sort(reverse=True)
    return result
