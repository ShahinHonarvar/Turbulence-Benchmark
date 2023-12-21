
import sympy

def all_left_truncatable_prime(t):
    x = t[33]
    result_list = [2, 3, 5, 7] if x > 7 else []
    
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def check(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    
    for candidate in range(10, x):
        if is_prime(candidate) and check(candidate):
            result_list.append(candidate)
    
    return sorted(result_list)
