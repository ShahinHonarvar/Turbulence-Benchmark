
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[466]
    lst = []
    for i in range(2, x):
        if isprime(i) and '0' not in str(i):
            number = str(i)
            while number != '':
                if isprime(int(number)):
                    number = number[1:]
                else:
                    break
            else:
                lst.append(i)
    lst.sort(reverse=True)
    return lst
