
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[25]
    
    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        else:
            return all(isprime(int(str(num)[i:])) for i in range(len(str(num))))
    
    lst = [i for i in range(x) if is_left_truncatable_prime(i)]
    lst.sort(reverse=True)
    return lst
