
def all_right_truncatable_prime(tup):
    import sympy
    x=tup[792]
    def right_truncatable_prime(num):
        num=str(num)
        for j in range(len(num)):
            if not sympy.isprime(int(num[j:])):
                return False
        return True
    list_of_primes=[]
    for i in range(2,x):
        if right_truncatable_prime(i):
            list_of_primes.append(i)
    return sorted(list_of_primes)
