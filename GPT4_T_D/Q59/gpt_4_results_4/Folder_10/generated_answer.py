
from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[38]
    result = []
    for i in range(11, x):
        if '0' in str(i):
            continue
        if all(isprime(int(str(i)[j:])) for j in range(len(str(i)))):
          result.append(i)
    return sorted(result, reverse=True)
