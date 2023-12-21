
def all_right_truncatable_prime(numbers):
    x = numbers[55]
    primes = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)
