
from itertools import permutations
from sympy import isprime

def all_left_right_truncatable_prime(lst):
    x = lst[92]
    primes = ['23', '37', '53', '73', '313', '373', '757']
    result = []
    digits = '123456789'
    for i in range(1, len(str(x)) + 1):
        for n in permutations(digits, i):
            num = ''.join(n)
            if int(num) > x:
                break
            if num in primes:
                result.append(int(num))
            elif isprime(int(num)):
                test = True
                for j in range(1, len(num)):
                    if not isprime(int(num[j:])) or not isprime(int(num[:-j])):
                        test = False
                        break
                if test:
                    primes.append(num)
                    result.append(int(num))
    return sorted(result)
