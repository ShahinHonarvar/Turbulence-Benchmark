
def all_left_truncatable_prime(t):
    from sympy import isprime

    x = t[37]
    primes_below_x = [i for i in range(2, x) if isprime(i) and '0' not in str(i)]

    def is_left_truncatable_prime(num):
        
        str_num = str(num)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True

    left_truncatable_primes = [p for p in primes_below_x if is_left_truncatable_prime(p)]
    left_truncatable_primes.sort(reverse=True)

    return left_truncatable_primes
