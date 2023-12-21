
def all_left_right_truncatable_prime(numbers):
    
    from sympy import isprime

    def is_truncatable(p):
        str_p = str(p)
        return all(isprime(int(str_p[i:]))
                and isprime(int(str_p[:len(str_p)-i]))
                for i in range(len(str_p)))
                
    x = numbers[14]
    truncatable_primes = [p for p in range(10, x+1)
                if set(str(p)) <= set('123456789')
                and is_truncatable(p)]
                
    return sorted(truncatable_primes)
