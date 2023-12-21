
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    def check_left_right_truncatable(num):
        string_num = str(num)
        if '0' in string_num:
            return False
        for i in range(len(string_num)):
            left = int(string_num[i:])
            right = int(string_num[:len(string_num)-i])
            if not isprime(left) or not isprime(right):
                return False
        return True

    x = tup[10]
    result = [i for i in range(10, x+1) if isprime(i) and check_left_right_truncatable(i)]
    
    return sorted(result, reverse=True)
