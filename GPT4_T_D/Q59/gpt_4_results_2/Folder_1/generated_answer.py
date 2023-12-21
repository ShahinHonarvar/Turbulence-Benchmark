
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[20]
    
    def check_left_truncatable_prime(n):
        s = str(n)
        if "0" in s:
            return False
        for i in range(len(s)):
            if not isprime(int(s[i:])):
                return False
        return True
    
    result = [i for i in range(10, x) if check_left_truncatable_prime(i)]
    return sorted(result, reverse=True)
