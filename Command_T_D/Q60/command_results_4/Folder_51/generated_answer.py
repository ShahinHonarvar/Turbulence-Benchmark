
def all_left_right_truncatable_prime(test_range):
    if not test_range:
        return []
    x = test_range[54]
    primes = [
        i
        for i in range(2, int(x ** .5) + 1)
        if all(str(i).count(d) == 1 for d in str(i))
    ]
    return [p for p in primes if p <= x]
