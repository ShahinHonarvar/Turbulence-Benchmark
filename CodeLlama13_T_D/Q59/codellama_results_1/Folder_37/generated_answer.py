
def all_left_truncatable_prime(numbers):
    x = numbers[35]
    primes = []
    for i in range(x):
        if is_prime(i) and not any(str(i).startswith('0') for i in str(i)):
            primes.append(i)
    return sorted(primes, reverse=True)
