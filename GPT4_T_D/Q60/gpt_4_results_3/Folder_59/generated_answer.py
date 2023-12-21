
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    def is_truncatable(n):
        str_n = str(n)
        return all(isprime(int(str_n[i:])) and isprime(int(str_n[:len(str_n)-i])) for i in range(len(str_n)))
                    
    x = numbers[84]
    return sorted([num for num in range(10, x+1) if '0' not in str(num) and isprime(num) and is_truncatable(num)], reverse=True)
