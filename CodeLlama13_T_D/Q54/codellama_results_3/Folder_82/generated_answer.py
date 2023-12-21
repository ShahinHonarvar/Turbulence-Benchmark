
def all_right_truncatable_prime(numbers):
    x = numbers[69]
    right_truncatable_primes = []
    for i in range(x):
        if is_prime(i) and is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
