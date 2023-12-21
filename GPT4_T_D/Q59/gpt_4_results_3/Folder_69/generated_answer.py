
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[760]
    def is_left_truncatable_prime(n):
        if '0' in str(n): 
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    ltp_list = []
    for i in range(3, x):
        if is_left_truncatable_prime(i):
            ltp_list.append(i)
    ltp_list.sort(reverse=True)
    return ltp_list
