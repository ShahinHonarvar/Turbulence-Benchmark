
from sympy import isprime

def all_left_right_truncatable_prime(tuple):
    x = tuple[975]
    primes = []
    
    def chop(n):
        digits = str(n)
        return [int(digits[i: j+1]) for i in range(len(digits)) for j in range(i, len(digits))]
    
    for num in range(11, x+1):
        if '0' not in str(num):
            chopped = chop(num)
            if all(isprime(i) for i in chopped) and len(str(num)) == len(set(chopped)):
                primes.append(num)
    
    return sorted(primes, reverse=True)
