
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[792]
    prime_numbers = []
    
    for i in range(10**6, x+1):
        if is_prime(i) and not has_zero(str(i)):
            prime_numbers.append(i)
            
    left_truncatable_primes = []
    right_truncatable_primes = []
    
    for i in prime_numbers:
        if is_left_truncatable_prime(str(i)):
            left_truncatable_primes.append(i)
        if is_right_truncatable_prime(str(i)):
            right_truncatable_primes.append(i)
            
    return sorted(set(left_truncatable_primes + right_truncatable_primes))
    
def has_zero(s):
    return '0' in s
    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def is_left_truncatable_prime(s):
    while len(s) > 1:
        if not is_prime(int(s)):
            return False
        s = s[1:]
    return True
    
def is_right_truncatable_prime(s):
    while len(s) > 1:
        if not is_prime(int(s)):
            return False
        s = s[:-1]
    return True
