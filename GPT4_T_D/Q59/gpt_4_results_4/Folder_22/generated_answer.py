
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[85]
    prime_list = []
    for i in range(11, x):
        if isprime(i) and '0' not in str(i):
            truncatable_check = True
            for j in range(len(str(i))):
                if not isprime(int(str(i)[j:])):
                    truncatable_check = False
                    break
            if truncatable_check:
                prime_list.append(i)
    return sorted(prime_list)
