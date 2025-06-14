
def all_left_right_truncatable_prime(tuple):
    x = tuple[52]
    primes = []
    for i in range(x+1):
        if is_prime(i) and str(i).find('0') == -1:
            primes.append(i)
    truncatable_primes = []
    for prime in primes:
        left = int(str(prime)[1:])
        right = int(str(prime)[:-1])
        if is_prime(left) and is_prime(right):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)
