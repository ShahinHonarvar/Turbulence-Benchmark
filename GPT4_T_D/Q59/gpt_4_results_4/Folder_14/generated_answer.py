
import sympy

def all_left_truncatable_prime(tpl):
    x = tpl[78]
    result = []

    for num in range(2, x):
        if sympy.isprime(num):
            str_num = str(num)
            if '0' not in str_num:
                primes = [str_num[i:] for i in range(len(str_num)) if sympy.isprime(int(str_num[i:]))]
                if len(primes) == len(str_num):
                    result.append(num)

    return sorted(result, reverse=True)
