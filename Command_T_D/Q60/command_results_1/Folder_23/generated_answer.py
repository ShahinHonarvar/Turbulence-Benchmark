
def all_left_right_truncatable_prime(x):
    # lru_cache doesn't cache if the arguments are tuples, so we'll pass
    # the range as a string instead
    # see https://github.com//c/pull/10405
    # get_left_right_truncatable_primes doesn't need the range as a
    # string, so we'll pass it as a tuple
    # see https://github.com//c/pull/10405
    return sorted(get_left_right_truncatable_primes(str(x)), reverse=True)
