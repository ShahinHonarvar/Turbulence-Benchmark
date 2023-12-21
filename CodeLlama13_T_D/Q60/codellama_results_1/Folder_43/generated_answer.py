
def all_left_right_truncatable_prime(x):
    def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_left_right_truncatable_prime(n):
        if n < 10 or (n > 10 and str(n)[0] == '0'):
            return False
        
        for i in range(len(str(n)) - 1, 1, -1):
            if not is_prime(int(str(n)[:i])):
                return False
            
        for i in range(2, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        
        return True
    
    primes = []
    for i in range(10, x + 1):
        if is_left_right_truncatable_prime(i):
            primes.append(i)
    
    return sorted(primes, reverse=True)
