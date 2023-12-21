
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_left_and_right_truncatable(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] == '0':
            return False
    for i in range(1, len(s)-1):
        if not is_prime(int(s[:i])*10+int(s[i+1:])):
            return False
    return True
