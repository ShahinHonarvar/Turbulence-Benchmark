
def all_left_right_truncatable_prime(tuple):
    x = tuple[803]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and contains_no_zeroes(str(i)) and left_and_right_truncatable(str(i)):
            primes.append(i)
    return sorted(primes)
