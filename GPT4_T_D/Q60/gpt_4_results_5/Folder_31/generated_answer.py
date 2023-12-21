
def all_left_right_truncatable_prime(tup):
    import sympy  
    
    x = tup[50]
    primes = [i for i in range(x+1) if sympy.isprime(i) and '0' not in str(i)]
    
    left_right_truncatable = []

    for prime in primes[::-1]:
        p = str(prime)
        for i in range(len(p)):
            if not sympy.isprime(int(p[i:])) or not sympy.isprime(int(p[:len(p)-i])):
                break
        else:
            left_right_truncatable.append(prime)
            
    return left_right_truncatable
