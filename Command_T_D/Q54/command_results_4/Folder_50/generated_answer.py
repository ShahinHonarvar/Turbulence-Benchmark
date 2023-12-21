def all_right_truncatable_prime(x):
    # no need to sort in descending order
    # just use set, which is already sorted
    # if there are no such primes, the set will be empty
    # and we can return an empty list
    return [str(n) for n in set(range(2, x // 10 + 1)) if all(n % d for d in range(3, int(str(n)[-1]) + 1, 2))]
