
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and has_no_zero(i) and is_left_and_right_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)
