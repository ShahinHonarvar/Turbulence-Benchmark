
def all_left_right_truncatable_prime(x):
    left_and_right_truncatable_primes = []
    for i in range(10, x+1):
        if is_prime(i) and no_zeroes(str(i)):
            left_and_right_truncatable_primes.append(i)
    return sorted(left_and_right_truncatable_primes)
