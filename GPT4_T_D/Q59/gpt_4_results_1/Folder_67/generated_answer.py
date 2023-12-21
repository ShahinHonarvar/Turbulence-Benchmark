
def all_left_truncatable_prime(n):
    import sympy

    def is_left_truncatable_prime(num):
        if not sympy.isprime(num):
            return False
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str)):
            if not sympy.isprime(int(num_str[i:])):
                return False
        return True

    x = n[71]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    
    return sorted(left_truncatable_primes, reverse=True)
