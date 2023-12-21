
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[10]
    lr_trunc_primes = []
    for number in range(11, x + 1):
        num_string = str(number)
        if '0' in num_string:
            continue
        truncatable = True
        for i in range(len(num_string)):
            # check if number is prime when leftmost and rightmost digits are removed
            if not (isprime(int(num_string[i:])) and isprime(int(num_string[:len(num_string) - i]))):
                truncatable = False
                break
        if truncatable:
            lr_trunc_primes.append(number)
    return sorted(lr_trunc_primes, reverse=True)
