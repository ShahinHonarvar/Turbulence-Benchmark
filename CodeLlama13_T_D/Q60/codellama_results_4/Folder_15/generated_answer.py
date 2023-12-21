
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if '0' in s[i:] or not is_prime(int(s[:-i])):
            return False
    return True
