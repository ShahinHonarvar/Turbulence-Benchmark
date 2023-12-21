
def all_left_truncatable_prime(tup):
    from sympy import primerange, isprime

    x = tup[7]
    primes = list(primerange(1, x))

    result = []
    for prime in primes:
        if '0' in str(prime):
            continue
        else:
            temp = str(prime)
            flag = True
            while len(temp) > 1:
                temp = temp[1:]
                if not isprime(int(temp)):
                    flag = False
                    break
            if flag:
                result.append(prime)

    result.sort()
    return result
