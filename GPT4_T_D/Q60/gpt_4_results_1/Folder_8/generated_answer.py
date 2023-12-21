
def all_left_right_truncatable_prime(input_tuple):
    import sympy
    x = input_tuple[41]

    lrt_primes = []
    for i in range(10, x+1):
        if '0' not in str(i):
            is_lrt_prime = True
            for j in range(len(str(i))):
                if not sympy.isprime(int(str(i)[j:])) or not sympy.isprime(int(str(i)[:len(str(i))-j])):
                    is_lrt_prime = False
                    break
            if is_lrt_prime:
                lrt_primes.append(i)
    lrt_primes.sort(reverse=True)
    return lrt_primes
