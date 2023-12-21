
from sympy import isprime

def all_right_truncatable_prime(tup):
    def is_right_truncatable(num):
        num = str(num)
        for i in range(len(num)):
            if not isprime(int(num[i:])):
                return False
        return True

    x = tup[1]
    rtn = [i for i in range(x) if is_right_truncatable(i)]
    return sorted(rtn, reverse=True)
