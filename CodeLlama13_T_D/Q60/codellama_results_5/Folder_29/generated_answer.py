
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and no_zero(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def no_zero(n):
    while len(str(n)) > 1 and n % 10 == 0:
        n //= 10
    return n != 0
