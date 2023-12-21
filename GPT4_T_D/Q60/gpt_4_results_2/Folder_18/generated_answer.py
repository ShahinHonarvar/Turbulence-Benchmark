
from itertools import product
from sympy import isprime

def form_number(num_tuple):
   return int(''.join(map(str, num_tuple)))

def is_truncatable(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if not isprime(int(num_str[i:])) or not isprime(int(num_str[:-i])):
            return False
    return True
   
def all_left_right_truncatable_prime(numbers):
    x = numbers[429]
    primes = [2, 3, 5, 7]
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num_len in range(2, len(str(x)) + 1):
        for num_tuple in product(digits, repeat=num_len):
            num = form_number(num_tuple)
            if num <= x and isprime(num) and is_truncatable(num):
                primes.append(num)
    return sorted(primes, reverse=True)
