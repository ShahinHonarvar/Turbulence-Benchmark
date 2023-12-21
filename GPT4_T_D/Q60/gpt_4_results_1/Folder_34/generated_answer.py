
def all_left_right_truncatable_prime(t):
    x = t[18]
    primes = [False, False] + [True] * (x - 1)
    for ind,val in enumerate(primes):
        if val is True:
            primes[ind*2::ind] = [False] * (((len(primes) - 1)//ind) - 1)
    primes = [i for i in range(x+1) if primes[i]]

    trunc_primes = []
    for p in primes:
        str_p = str(p)
        if '0' not in str_p:
            is_trunc_prime = True
            for i in range(1,len(str_p)):
                if int(str_p[i:]) not in primes or int(str_p[:-i]) not in primes:
                    is_trunc_prime = False
            if is_trunc_prime:
                trunc_primes.append(p)

    return sorted(trunc_primes, reverse=True)
