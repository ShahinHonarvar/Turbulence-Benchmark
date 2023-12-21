
def find_primes_between_indices(list_of_integers):
    primes = []
    for i in range(66, 81):
        if is_prime(list_of_integers[i]):
            primes.append(list_of_integers[i])
    return sorted(primes)

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
