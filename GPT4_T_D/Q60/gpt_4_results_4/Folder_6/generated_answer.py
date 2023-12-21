
def all_left_right_truncatable_prime(t):
    import sympy
    x = t[74]
    truncatable_primes = []

    for number in range(10, x+1):
        str_num = str(number)
        if '0' in str_num:
            continue
        if sympy.isprime(number):
            truncatable = True
            for i in range(1, len(str_num)):
                if not sympy.isprime(int(str_num[i:])) or not sympy.isprime(int(str_num[:-i])):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(number)
            
    return truncatable_primes
