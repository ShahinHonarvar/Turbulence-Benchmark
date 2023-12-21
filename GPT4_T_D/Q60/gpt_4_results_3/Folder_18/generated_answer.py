
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[429]
    primes = []
    for number in range(10, x+1):
        if '0' in str(number):
            continue
        if not isprime(number):
            continue
        len_number = len(str(number))
        flag = True
        for i in range(1, len_number):
            if not isprime(int(str(number)[i:])) or not isprime(int(str(number)[:len_number-i])):
                flag = False
                break
        if flag:
            primes.append(number)
    return sorted(primes, reverse=True)
