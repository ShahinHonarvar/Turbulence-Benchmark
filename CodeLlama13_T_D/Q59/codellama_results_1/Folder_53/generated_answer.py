
def all_left_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and not contains_zero(num):
            primes.append(num)
    return sorted(primes, reverse=True)
