
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[0]
    def check_prime(n):
        return isprime(n)
  
    def left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not check_prime(int(str_n[i:])):
                return False
        return True
    
    prime_list = [number for number in range(x) if '0' not in str(number) and check_prime(number) and left_truncatable(number)]
    prime_list.sort(reverse=True)
    return prime_list
