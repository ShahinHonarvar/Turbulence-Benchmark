
from sympy import isprime

def all_left_right_truncatable_prime(tuple_of_pos_integers):
    x = tuple_of_pos_integers[77]
    all_primes = list(filter(lambda num: isprime(num), range(11, x+1)))
    lr_truncatable_primes = []

    for num in all_primes:
        if '0' in str(num):
            continue
        length = len(str(num))
        is_lr_truncatable_prime = True

        for i in range(length):
            left_truncated = str(num)[i:]
            right_truncated = str(num)[:length-i]
            if not(isprime(int(left_truncated)) and isprime(int(right_truncated))):
                is_lr_truncatable_prime = False
                break

        if is_lr_truncatable_prime:
            lr_truncatable_primes.append(num)

    return sorted(lr_truncatable_primes, reverse=True)
