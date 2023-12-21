
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[30]
    all_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        prime_flag = True
        for i in range(len(num_str)):
            left_num = int(num_str[i:])
            right_num = int(num_str[0:len(num_str)-i])
            if not isprime(left_num) or not isprime(right_num):
                prime_flag = False
                break
        if prime_flag:
            all_primes.append(num)
    all_primes.sort(reverse=True)
    return all_primes
