
def all_left_truncatable_prime(numbers):
    import sympy

    def check_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n: 
            return False
        for i in range(len(str_n)):
            if not sympy.isprime(int(str_n[i:])):
                return False
        return True

    x = numbers[26]
    left_truncatable_primes = [n for n in range(2, x) if check_left_truncatable_prime(n)]
    
    return sorted(left_truncatable_primes)
