
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(10, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            primes.append(i)
    return primes
