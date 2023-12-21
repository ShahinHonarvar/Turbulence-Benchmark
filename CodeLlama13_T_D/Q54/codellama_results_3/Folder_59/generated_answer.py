
def all_right_truncatable_prime(x):
    primes = []
    for i in range(10**84, x+1):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_right_truncatable_prime(n):
    if n <= 1 or any(n % i == 0 for i in range(2, int(n**0.5) + 1)):
        return False
    for i in range(len(str(n))-1, -1, -1):
        if not is_prime(int(str(n)[:i])):
            return False
    return True

def is_prime(n):
    if n <= 1 or any(n % i == 0 for i in range(2, int(n**0.5) + 1)):
        return False
    return True
