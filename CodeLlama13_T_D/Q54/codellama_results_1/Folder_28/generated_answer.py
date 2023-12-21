
def all_right_truncatable_prime(numbers):
    x = numbers[19]
    primes = []
    for i in range(2, x+1):
        if is_prime(i):
            primes.append(i)
    truncatable_primes = []
    for p in primes:
        n = p
        while n > 0:
            n //= 10
            if not is_prime(n):
                break
        else:
            truncatable_primes.append(p)
    return sorted(truncatable_primes)
