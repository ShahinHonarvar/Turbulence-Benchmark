
def all_left_right_truncatable_prime(numbers):
    x = numbers[26]
    left_truncatable_primes = []
    right_truncatable_primes = []
    
    for i in range(x+1):
        if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            left_truncatable_primes.append(i)
            right_truncatable_primes.append(i)
    
    return sorted(list(set(left_truncatable_primes + right_truncatable_primes)))

def is_left_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(int(str(n)[1:] or 0)):
        if not is_prime(i) and n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(int(str(n)[:-1] or 0)):
        if not is_prime(i) and n % i == 0:
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
