
def all_right_truncatable_prime(numbers):
    x = numbers[39]
    primes = []
    for i in range(x):
        if is_prime(i) and is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)
