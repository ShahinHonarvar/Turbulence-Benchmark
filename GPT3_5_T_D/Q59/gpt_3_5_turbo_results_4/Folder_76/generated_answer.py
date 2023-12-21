
import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[370]
    result = []
    
    def is_prime(n):
        return sympy.isprime(n)
    
    def is_left_truncatable_prime(n):
        num = str(n)
        while num:
            if not is_prime(int(num)):
                return False
            num = num[1:]
        return True
    
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    
    return sorted(result, reverse=True)
