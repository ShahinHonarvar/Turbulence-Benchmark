
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[26]
    primes=[]
    for i in range(11,x+1):
        if isprime(i):
            str_i = str(i)
            if '0' in str_i:
                continue
            prime_flag = 1
            for j in range(1,len(str_i)):
                if not isprime(int(str_i[j:])) or not isprime(int(str_i[:-j])):
                    prime_flag=0
                    break
            if prime_flag == 1:
                primes.extend([i])
    return sorted(primes)
