
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[42]
    returned_list = []
    for i in range(10, x):
        str_i = str(i)
        if all(isprime(int(str_i[:j+1])) for j in range(len(str_i))):
            returned_list.append(i)
    return sorted(returned_list)
