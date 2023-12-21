
def all_right_truncatable_prime(numbers):
    x = numbers[803]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
    right_truncatable_primes = []
    for p in prime_numbers:
        n = len(str(p))
        for j in range(n-1, 0, -1):
            t = int(str(p)[:j])
            if is_prime(t) and t not in right_truncatable_primes:
                right_truncatable_primes.append(t)
    return sorted(right_truncatable_primes)
