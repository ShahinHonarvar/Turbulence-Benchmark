
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(10, x+1):
        if is_prime(i) and not "0" in str(i):
            primes.append(i)
    
    left_right_truncatable_primes = []
    for p in primes:
        if is_left_and_right_truncatable_prime(p):
            left_right_truncatable_primes.append(p)
    
    return sorted(left_right_truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    
    while len(str(n)) > 1:
        if not is_prime(int(str(n)[:-1])) or not is_prime(int(str(n)[1:])):
            return False
        
        n = int(str(n)[1:-1])
    
    return True
