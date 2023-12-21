
from sympy import isprime

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[54]
    prime_numbers = []
    for number in range(1, x):
        str_num = str(number)
        is_truncatable_prime = True
        while len(str_num) > 0:
            if isprime(int(str_num)):
                str_num = str_num[:-1]
            else:
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            prime_numbers.append(number)
    prime_numbers.sort(reverse=True)
    return prime_numbers
