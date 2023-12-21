
def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and not contains_zero(str(num)):
            primes.append(num)
    return sorted(primes, reverse=True)
