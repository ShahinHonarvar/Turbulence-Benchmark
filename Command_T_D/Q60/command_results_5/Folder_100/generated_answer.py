
import itertools

def all_left_right_truncatable_prime(x):
    for p in itertools.permutations(range(2, x), 2):
        s = str(p)
        if not s[0] == '0':
            yield int(s)
            continue
        for i in range(1, len(s)-1):
            if s[i] == '0':
                break
            yield int(s[:i]+s[i+1:])
            break
    return sorted(list(set(x.get_left_right_truncatable_primes())))
