
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_left_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)

def is_left_right_truncatable_prime(n):
    if n < 2 or (n % 2 == 0 and n != 2):
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
