
def all_right_truncatable_prime(numbers):
    x = numbers[630]
    right_truncatable_primes = []
    for i in range(x-1, 0, -1):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
