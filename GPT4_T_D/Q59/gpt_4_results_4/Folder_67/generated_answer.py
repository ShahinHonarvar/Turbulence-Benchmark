
from sympy import isprime

def all_left_truncatable_prime(tup):
    if len(tup) < 72 or not isinstance(tup[71], int):
        return "Invalid input"

    x = tup[71]

    def left_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    result = [i for i in range(x) if left_truncatable(i)]
    result.sort(reverse=True)

    return result
