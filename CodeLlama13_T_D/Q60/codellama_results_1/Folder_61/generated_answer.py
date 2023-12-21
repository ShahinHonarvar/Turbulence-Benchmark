
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_left_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_left_right_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    while len(str(n)) > 3:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
