
def all_left_right_truncatable_prime(tuple):
    import sympy
    x = tuple[67]
    truncatable_primes = []
    for i in range(10, x+1):
        str_num = str(i)
        if '0' in str_num:
            continue
        left_right_truncatable = True
        for j in range(len(str_num)):
            if not (sympy.isprime(int(str_num[j:])) and sympy.isprime(int(str_num[:len(str_num)-j]))):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
