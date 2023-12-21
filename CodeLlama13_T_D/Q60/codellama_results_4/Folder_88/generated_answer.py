
def all_left_right_truncatable_prime(tuple):
    x = tuple[93]
    left_right_truncatable_primes = []
    for i in range(2, x+1):
        if is_left_and_right_truncatable_prime(i, x):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)

def is_left_and_right_truncatable_prime(n, x):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(x**0.5)+1):
        if n % i == 0:
            return False
    return True
