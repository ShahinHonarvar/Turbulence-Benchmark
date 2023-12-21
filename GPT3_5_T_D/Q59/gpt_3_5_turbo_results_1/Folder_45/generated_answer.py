
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[61]
    num_list = []

    def is_left_truncatable_prime(num):
        str_num = str(num)

        for i in range(len(str_num)):
            curr_num = int(str_num[i:])
            if not isprime(curr_num):
                return False
        return True

    for i in range(11, x):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            num_list.append(i)

    return sorted(num_list)
