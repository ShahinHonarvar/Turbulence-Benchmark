
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[33]
    left_right_truncatable_primes = []
    for i in range(2, x+1):
        if is_left_and_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)

def is_left_and_right_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(10**5):
        if not is_prime(n*10**i+i):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
