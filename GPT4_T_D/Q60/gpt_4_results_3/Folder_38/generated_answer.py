
from itertools import permutations
from sympy import isprime

def all_left_right_truncatable_prime(integers):
    
    def l_r_truncable(num):
        temp = str(num)
        if "0" in temp or num < 10:
            return False
        length = len(temp)
        for x in range(length):
            if not(isprime(int(temp[x:]))) or not(isprime(int(temp[:(length-x)]))):
                return False
        return True
    
    x = integers[28]
    primes_permutation = []
    for i in range(1, len(str(x))+1):
        for j in permutations('123456789', i):
            primes_permutation.append(int(''.join(j)))

    all_truncable_primes = [i for i in primes_permutation if l_r_truncable(i)]
    all_truncable_primes = [i for i in all_truncable_primes if i <= x]

    all_truncable_primes.sort()

    return all_truncable_primes
