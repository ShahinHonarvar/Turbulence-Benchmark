
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    primes = []

    def check_prime(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])) or not isprime(int(str_num[:len(str_num)-i])):
                return False
        return True

    for num in range(10, x+1):
        if '0' not in str(num) and check_prime(num):
            primes.append(num)

    return sorted(primes, reverse=True)
