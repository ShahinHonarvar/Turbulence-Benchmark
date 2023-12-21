
def all_right_truncatable_prime(x):
    primes = []
    for i in range(10**7, x+1):
        if is_prime(i) and is_truncatable_prime(str(i)):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(s):
    while s != '':
        if not is_prime(int(s)):
            return False
        s = s[:-1]
    return True
