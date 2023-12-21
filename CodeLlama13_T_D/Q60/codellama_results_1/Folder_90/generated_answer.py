
def all_left_right_truncatable_prime(numbers):
    primes = []
    for n in numbers:
        if n <= 10 or n % 10 == 5: continue
        if not any([n % i for i in range(2, int(n ** 0.5) + 1)]):
            primes.append(n)
    return sorted(primes, reverse=True)
