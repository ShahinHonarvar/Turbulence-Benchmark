
from sympy import isprime

def all_right_truncatable_prime(t):
    prime_list = []
    x = t[55]

    for num in range(2, x):
        str_num = str(num)
        is_trunc_prime = True
        for i in range(len(str_num)):
            if not isprime(int(str_num)):
                is_trunc_prime = False
                break
            str_num = str_num[:-1]
        if (is_trunc_prime):
            prime_list.append(num)

    prime_list.sort(reverse=True)
    return prime_list
