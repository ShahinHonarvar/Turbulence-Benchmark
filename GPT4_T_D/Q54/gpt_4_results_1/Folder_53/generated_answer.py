
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(n):
    num = str(n)
    for i in range(len(num)):
        if not is_prime(int(num[:len(num) - i])):
            return False
    return True        

def all_right_truncatable_prime(t):
    x = t[86]
    truncatable_primes = [
        i for i in range(1, x) if is_right_truncatable_prime(i)
    ]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
