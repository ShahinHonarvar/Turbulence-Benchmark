
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[:len(str_n) - i])):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[618]
    primes = []
    for i in range(2, x):
        if is_right_truncatable(i):
            primes.append(i)
    primes.sort()
    return primes
