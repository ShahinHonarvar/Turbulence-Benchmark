
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[20]
    results = []

    def is_left_truncatable(num):
        str_num = str(num)
        if '0' in str_num: return False
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True

    for num in range(2, x):
        if is_left_truncatable(num):
            results.append(num)

    results.sort(reverse=True)
    return results
