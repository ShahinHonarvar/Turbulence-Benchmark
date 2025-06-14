
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[92]
    left_truncatable_primes = []
    for i in range(x+1):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)

def is_left_truncatable_prime(n):
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True
