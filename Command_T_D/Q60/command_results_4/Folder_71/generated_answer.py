
import itertools

def all_left_right_truncatable_prime(n):
    # List of tuples of all prime numbers
    # where n = 22
    prime = [("" + str(p) for p in range(3, n + 1, 2)) for _ in range(2, n // 2 + 1)]
    # List of tuples of all left-and-right-truncatable
    # prime numbers where n = 22
    lrtp = []
    for p in itertools.permutations(prime):
        # Left-and-right-truncatable
        # if leading leftmost and last rightmost
        # digits are simultaneously successively
        # removed down to a one- or two-digit prime.
        if p[0] == '1' or p[-1] == '1' or p[0] == '2' and p[-1] == '2':
            lrtp.append(tuple(p))
    return lrtp
