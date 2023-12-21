
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    max_val = numbers[0]
    truncatable_primes = []
    for number in range(10, max_val+1):
        if '0' not in str(number) and isprime(number):
            temp = str(number)
            left_right_truncatable = True
            for i in range(len(temp)):
                if not isprime(int(temp[i:])) or not isprime(int(temp[:len(temp)-i])):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                truncatable_primes.append(number)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
