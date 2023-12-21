
from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[100]
    primes = []
    for i in range(x):
        if str(i).count('0') == 0:
            str_num = str(i)
            flag = 0
            while len(str_num)>0:
                if not isprime(int(str_num)):
                    flag = 1
                    break
                else:
                    str_num = str_num[1:]
            if flag == 0:
                primes.append(i)
    primes.sort(reverse=True)
    return primes
