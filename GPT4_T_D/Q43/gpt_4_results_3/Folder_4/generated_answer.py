
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n%i == 0 or n%(i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_between_indices(list_of_integers):
    primes_in_range = [num for num in list_of_integers[24:84] if is_prime(num)]
    primes_in_range.sort()
    return primes_in_range
