
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[37]
    prime_list = []
    for number in range(10, x+1):
        if '0' in str(number):
            continue
        left_right_prime = True
        for i in range(len(str(number))):
            if not (isprime(int(str(number)[i:])) and isprime(int(str(number)[:len(str(number))-i]))):
                left_right_prime = False
                break
        if left_right_prime:
            prime_list.append(number)
    return sorted(prime_list, reverse=True)
