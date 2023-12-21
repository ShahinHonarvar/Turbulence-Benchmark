
import math

def all_left_truncatable_prime(tup):
    x = tup[86]
    is_prime = lambda num: all(num%i != 0 for i in range(2, int(math.sqrt(num))+1))
    is_left_truncatable = lambda num: all(is_prime(int(str(num)[i:])) for i in range(len(str(num))))
    primes = []
    for number in range(2, x):
        if '0' not in str(number) and is_prime(number) and is_left_truncatable(number):
            primes.append(number)
    return sorted(primes, reverse=True)
