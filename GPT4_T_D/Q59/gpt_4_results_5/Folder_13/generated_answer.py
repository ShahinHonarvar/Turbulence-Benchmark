
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[784]
    primes = [i for i in range(2, x) if is_prime(i)]
    result = [i for i in primes if is_left_truncatable_prime(i)]
    result.sort()    
    return result
