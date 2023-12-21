import re
import itertools
def all_left_truncatable_prime(num_tup):
    return [
        n for n in range(num_tup[29])
        if all(a % 10 == b for a, b in zip(str(n), str(n + 1)))
        and left_truncatable_prime_re.search(str(n))
    ]
