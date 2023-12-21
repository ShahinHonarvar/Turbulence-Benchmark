
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[8]
    truncatable_primes = []
    for num in range(11, x+1):
        str_num = str(num)
        if '0' in str_num: 
            continue
        left_truncatables = [int(str_num[i:]) for i in range(len(str_num))]
        right_truncatables = [int(str_num[:i]) for i in range(len(str_num), 0, -1)]
        if all(isprime(num) for num in left_truncatables + right_truncatables):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
