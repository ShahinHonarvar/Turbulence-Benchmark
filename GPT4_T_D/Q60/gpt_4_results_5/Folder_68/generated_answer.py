
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[1]
    truncatable_primes = []
    for i in range(11, x + 1):
        if '0' in str(i):
            continue
        else:
            str_num = str(i)
            count = 0
            for j in range(len(str_num)):
                if isprime(int(str_num[j:])) and isprime(int(str_num[:len(str_num) - j])):
                    count += 1
                else:
                    break
            if count == len(str_num):
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
