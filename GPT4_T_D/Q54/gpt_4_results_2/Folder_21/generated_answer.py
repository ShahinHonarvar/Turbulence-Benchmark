
import sympy

def all_right_truncatable_prime(tuple_):
    x = tuple_[175]
    truncatable_primes = []
    for num in range(1, x):
        str_num = str(num)
        str_list = list(str_num)
        for i in range(len(str_list)):
            str_check = ''.join(str_list[i:])
            if not sympy.isprime(int(str_check)):
                break
        else:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)
