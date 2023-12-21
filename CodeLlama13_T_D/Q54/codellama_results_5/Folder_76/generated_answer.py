
def all_right_truncatable_prime(x):
    right_truncatable_primes = []
    for i in range(10**x-1, 10**(x-1)-1):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_right_truncatable_prime(n):
    if n % 10 == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 and is_right_truncatable_prime(n//i):
            return True
    return False
