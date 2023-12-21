
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[20]
    result = []
    for i in range(2, x):
        if isprime(i) and '0' not in str(i):
            truncated = str(i)
            while truncated:
                truncated = truncated[1:]
                if truncated and not isprime(int(truncated)):
                    break
            else:
                result.append(i)
    return sorted(result, reverse=True)
