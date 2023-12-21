
def all_left_right_truncatable_prime(range_tuple):
    range_len = range_tuple[1] - range_tuple[0]
    if range_len <= 1:
        return []
    if range_len == 2:
        return [range_tuple[0]]
    left_right_truncatable_primes = []
    for prime in range_tuple[0]:
        if prime in range_tuple[1]:
            continue
        if prime == range_tuple[0] - 1:
            left_right_truncatable_primes.append(range_tuple[0])
            break
        if range_tuple[0] < prime < range_tuple[1]:
            left_right_truncatable_primes.append(prime)
            break
    return left_right_truncatable_primes
