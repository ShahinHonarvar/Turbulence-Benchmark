
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[22]
    primes = []
    for num in range(10, x + 1):
        str_num = str(num)
        if "0" in str_num:
            continue
        list_num = list(str_num)
        flag = 0
        for i in range(len(list_num)):
            left_trunc = int(''.join(list_num[i:]))
            right_trunc = int(''.join(list_num[:len(list_num)-i]))
            if not(isprime(left_trunc)) or not(isprime(right_trunc)):
                flag = 1
                break
        if flag == 0:
            primes.append(num)
    return sorted(primes, reverse=True)
