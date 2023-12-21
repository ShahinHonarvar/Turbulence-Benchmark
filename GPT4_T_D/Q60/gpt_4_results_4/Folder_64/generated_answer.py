
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[4]
    num_list = []

    def check_truncatable(num):
        if len(num) <= 2 and isprime(int(num)):
            return True
        else:
            if isprime(int(num)) and '0' not in num:
                return check_truncatable(num[1:-1])
            else:
                return False

    for num in range(10, x+1):
        if check_truncatable(str(num)):
            num_list.append(num)

    return sorted(num_list)
