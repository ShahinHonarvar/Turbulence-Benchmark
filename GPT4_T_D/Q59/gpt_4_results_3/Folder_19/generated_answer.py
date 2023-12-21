
from sympy import isprime

def all_left_truncatable_prime(tup):
    if len(tup) <= 67:
        return "Tuple is less than 68 elements"
    x = tup[67]
    left_truncatable_primes = []
    
    for num in range(2, x):
        if '0' in str(num): 
            continue
        else:
            num_str = str(num)
            count = len(num_str)
            for i in range(len(num_str)):
                if isprime(int(num_str[i:])):
                    count -= 1
            if count == 0:
                left_truncatable_primes.append(num)

    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
