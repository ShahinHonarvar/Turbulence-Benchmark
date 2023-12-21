
def all_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and is_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)
