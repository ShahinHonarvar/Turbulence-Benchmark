
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[50]
    results = []
    for i in range(x-1, 2, -1):
        str_i = str(i)
        if '0' in str_i:
            continue
        is_truncatable_prime = True
        for j in range(len(str_i)):
            if not isprime(int(str_i[j:])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            results.append(i)
    return results
