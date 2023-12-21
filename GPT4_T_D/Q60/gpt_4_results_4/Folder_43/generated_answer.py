
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    def check_truncatable(n):
        str_n = str(n)
        return all(isprime(int(str_n[i:len(str_n)-i])) for i in range(len(str_n)))
    
    x = numbers[89]

    return sorted([i for i in range(10, x+1) if '0' not in str(i) and isprime(i) and check_truncatable(i)], reverse=True)
