import itertools
import re
import string
def all_left_truncatable_prime(num_tup):
    x = num_tup[61]
    return sorted(set(
        int(p)
        for p in itertools.permutations(
            (s for s in range(2, x) if all(int(d) for d in str(s))),
            num_tup[0],
            num_tup[1],
        )
        for s in range(2, x)
        if not left_re.match(str(s))
        and all(right_re.match(str(d) for d in str(s)))
    ))
