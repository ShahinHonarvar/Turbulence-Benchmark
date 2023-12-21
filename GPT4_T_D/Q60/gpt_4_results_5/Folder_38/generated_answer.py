
from sympy import isprime

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[28]
    result = []

    def check_truncatable(num):
        string_num = str(num)
        length = len(string_num)
        
        for i in range(length):
            if not isprime(int(string_num[i:])) or not isprime(int(string_num[:length-i])) or '0' in string_num:
                return False
        return True

    for number in range(11, x+1):
        if check_truncatable(number):
            result.append(number)

    result.sort()
    return result
