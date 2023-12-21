
def all_right_truncatable_prime(t):
    x = t[67]
    primes = []
    for num in range(2, x):
        if all(num % i != 0 for i in range(2, num)):
            primes.append(num)
    right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        while len(str_prime) > 0:
            if all(int(str_prime) % i != 0 for i in range(2, int(str_prime))):
                str_prime = str_prime[:-1]
            else:
                break
        if len(str_prime) == 0:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)
