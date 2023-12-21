
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[11]
    result = []
    for i in range(10, x):
        str_i = str(i)
        if '0' in str_i:
            continue
        prime_flag = True
        for j in range(len(str_i)):
            if not isprime(int(str_i[j:])):
                prime_flag = False
                break
        if prime_flag:
            result.append(i)
    return sorted(result)
