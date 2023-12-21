
def all_left_right_truncatable_prime(tuple):
    primes = []
    for num in tuple:
        if is_left_and_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)
