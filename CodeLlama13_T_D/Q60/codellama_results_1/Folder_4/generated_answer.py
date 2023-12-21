
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_left_and_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_left_and_right_truncatable_prime(n):
    if n % 2 == 0 or n < 3:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
