
from sympy import isprime

def all_left_truncatable_prime(tuple_of_int):
    x = tuple_of_int[86]
    prime_nums = []
    for number in range(10, x):
        if '0' not in str(number) and isprime(number):
            temp = str(number)
            while len(temp) > 1:
                temp = temp[1:]
                if not isprime(int(temp)):
                    break
            else:
                prime_nums.append(number)
    return sorted(prime_nums)
